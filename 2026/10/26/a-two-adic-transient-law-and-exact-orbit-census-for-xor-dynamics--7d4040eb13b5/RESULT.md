# A two-adic transient law and exact orbit census for XOR dynamics on wheel graphs

## Finding

For every integer \(n\ge3\), let \(W_n=K_1\vee C_n\) have an \(n\)-vertex rim and one hub. A synchronous binary state at every vertex is replaced by the sum of its **open-neighbour** states in \(\mathbb F_2\); denote this linear update by \(F_n\). Let \(k=2^{\nu_2(n)}\) be the largest power of two dividing \(n\), with \(k=1\) for odd \(n\). All polynomial operations in the following formulas are over \(\mathbb F_2[z]\). Set

\[
q_n(z)=\frac{z^n+1}{(z+1)^k},\qquad H_t(z)=(z^2+1)^t+z^t\quad(t\ge1).
\]

Then the **exact temporal fixed-point count for every positive time** is

\[
\#\operatorname{Fix}(F_n^t)
=2^{\deg\gcd(q_n,H_t)+\epsilon_n(t)},\qquad
\epsilon_n(t)=
\begin{cases}
1,&n\text{ odd},\ t\text{ odd},\\
2,&n\text{ odd},\ t\text{ even},\\
0,&n\text{ even}.
\end{cases}
\]

Here \(\deg\gcd(1,H_t)=0\). Consequently the exact number of primitive temporal cycles of length \(t\) is

\[
\frac1t\sum_{d\mid t}\mu(t/d)\,\#\operatorname{Fix}(F_n^d),
\]

where \(\mu\) is the number-theoretic Möbius function.

For odd \(n\), \(F_n\) is bijective, so **all \(2^{n+1}\) configurations are recurrent** and their preperiod is zero. For even \(n\), exactly \(2^{n-k}\) configurations are recurrent, and every recurrent cycle has a basin consisting of its own length multiplied by \(2^{k+1}\). The maximum number of updates before first entering a periodic orbit is **exactly**

\[
T_n=\begin{cases}
3,&k=2\text{ or }k=4,\\
k/2,&k\ge8.
\end{cases}
\]

In particular, even wheels with \(n\) a power of two have only the all-zero recurrent configuration, and their sharp extinction times are \(3\) for \(n=4\) and \(n/2\) for \(n\ge8\).

The entire convergence-time distribution is determined as follows. Write \(r_t=\operatorname{rank}_{\mathbb F_2}(F_n^t)\). For even \(n\),

\[
r_0=n+1,\qquad
r_1=\begin{cases}n,&k=2,\\n-2,&k\ge4,\end{cases}
\]
\[
r_2=\begin{cases}n-1,&k=2,\\n-3,&k=4,\\n-4,&k\ge8,\end{cases}
\qquad
r_t=n-\min(2t,k)\quad(t\ge3).
\]

The number of initial states whose **least preperiod is at most** \(t\ge0\) equals

\[
E_n(t)=2^{n+1-r_t+(n-k)}.
\]

Thus the exact number of initial states with least preperiod \(t\) is \(E_n(0)\) if \(t=0\), and \(E_n(t)-E_n(t-1)\) if \(t\ge1\). For odd \(n\), \(r_t=n+1\) and \(E_n(t)=2^{n+1}\) for all \(t\ge0\).

## Assumptions and scope

The graph is finite, labelled, simple and undirected. The rim is a cycle with distinct neighbours at every vertex, including \(n=3\), and the hub is adjacent to every rim vertex. Arithmetic is exclusively binary XOR: no self-state is added, no majority threshold is imposed, and updates are simultaneous. All formulas apply for every stated \(n\) and \(t\), not only tested parameter ranges. Temporal fixed points refer to the full state, including the hub. Periodic points are those on cycles, rather than merely eventually periodic points.

## Proof

**1. Polynomial reduction.** Identify the rim vector \(x\) with a polynomial in \(R_n=\mathbb F_2[z]/(z^n+1)\); let \(h\in\mathbb F_2\) be the hub state. Define the invertible residue \(z^{-1}\), the rim map \(B=z+z^{-1}=z^{-1}(z+1)^2\), the all-one rim vector \(J=1+z+\cdots+z^{n-1}\), and the parity functional \(S(x)=x(1)\). Then

\[
F_n(x,h)=(Bx+hJ,S(x)).
\]

As \(BJ=0\), \(S(Bx)=0\), and \(S(J)=n\bmod2\), direct composition gives

\[
F_n^2(x,h)=(B^2x+S(x)J,(n\bmod2)h).
\]

When \(n\) is even a further update gives the exact identity

\[
F_n^3(x,h)=(B^3x,0),\qquad
F_n^t(x,h)=(B^tx,0)\quad(t\ge3).
\]

**2. The primary decomposition.** Write \(n=km\), with \(m\) odd and \(k\) a power of two. In characteristic two,

\[
z^n+1=(z+1)^kq_n(z),\qquad \gcd(z+1,q_n)=1.
\]

The Chinese remainder theorem decomposes \(R_n\) into a primary component of dimension \(k\) at \(z=1\), and a complementary component of dimension \(n-k\). On the primary component, \(B\) is a unit times \((z+1)^2\); on the complementary component it is invertible. Therefore

\[
\operatorname{rank}(B^t)=n-\min(2t,k).
\]

The hub coupling \(J\) lies exclusively in the primary component and there generates its socle, proportional to \((z+1)^{k-1}\). The functional \(S\) extracts its constant term in the local coordinate \(z+1\). Thus the complementary component is the stable recurrent subspace when \(n\) is even.

**3. Even rims: exact ranks and transients.** For \(k=2\), \(J\) lies outside \(\operatorname{im}B\) and \(S\) is nonzero on the two-dimensional kernel of \(B\), so \((x,h)\mapsto(Bx+hJ,S(x))\) has rank \(n\). For \(k\ge4\), \(J\) lies in \(\operatorname{im}B\), has a preimage of parity zero, and \(S\) vanishes on \(\ker B\), so this map has rank \(n-2\). Likewise, from the displayed formula for \(F_n^2\), its rank is \(n-1\) for \(k=2\), \(n-3\) for \(k=4\), and \(n-4\) for \(k\ge8\): in the last case \(J\in\operatorname{im}B^2\) has a parity-zero preimage and \(S\) vanishes on \(\ker B^2\), so the induced rank-one modification of \(\operatorname{im}B^2\) is invertible (its square is the identity). For the first two cases the rim-parity-induced \(J\)-direction contributes an extra independent output. For \(t\ge3\), the identity in step 1 and the rank of \(B^t\) give the remaining rank formula.

The eventual image has dimension \(n-k\), and restriction to it is a bijection. The ranks stabilize for the first time at \(t=3\) when \(k=2\) or \(4\), and at \(t=k/2\) when \(k\ge8\). Since the preceding rank is strictly larger, these are attained maximum preperiods, not merely upper bounds. Every point on a cycle has exactly \(2^{k+1}\) full preimages under the eventual projection, giving the uniform basin factor. For any \(t\), \(F_n^t\) maps onto a space of dimension \(r_t\) containing the stable image, so the inverse image of the stable subspace has dimension \((n+1)-r_t+(n-k)\). This establishes \(E_n(t)\) and its differences.

**4. Odd rims and the periodic spectrum.** If \(n\) is odd, \(S(J)=1\), so each rim vector has the unique decomposition \(x=S(x)J+y\) with \(S(y)=0\). In these coordinates, \(F_n\) swaps the two bits \(S(x)\) and \(h\), while acting by \(B\) on the \((n-1)\)-dimensional zero-parity module. The latter is naturally isomorphic to \(\mathbb F_2[z]/(q_n(z))\), where \(B\) is invertible. Therefore \(F_n\) itself is invertible, and the swap contributes a \(1\)-dimensional \(t\)-fixed space for odd \(t\) and a \(2\)-dimensional one for even \(t\).

For even \(n\), the periodic subsystem is isomorphic to \(\mathbb F_2[z]/(q_n(z))\) with multiplication by \(B\), without a hub swap. In either case, \(B^t-I=z^{-t}H_t(z)\); because \(z\) is a unit modulo \(q_n\), the \(t\)-fixed-space dimension of this multiplication is exactly \(\deg\gcd(q_n,H_t)\). This proves the fixed-point formula. Möbius inversion of the count of points whose primitive period divides \(t\) proves the exact cycle formula.

## Verification

Run `python3 verify.py` using only Python's standard library. The supplied program constructs the original binary wheel adjacency map independently of the polynomial derivation. It compares the predicted rank of every iterate against independent binary Gaussian elimination for \(3\le n\le60\), and evaluates fixed-state counts using two distinct methods for \(1\le t\le20\). It also enumerates all binary states for \(3\le n\le10\), checks their least preperiods and primitive cycle lengths, and checks the entire preperiod distribution. The recorded output is `verification_output.txt`, with a successful final status of `VERIFY_OK`. These finite checks are corroboration; the preceding algebraic proof establishes the unrestricted assertions.

## Relationship to prior work

Klaus Sutner, *Additive Automata on Graphs* (1988), develops open-neighbourhood XOR automata on undirected graphs and examines predecessor existence and reversibility. Ciandrini et al., *Feedback topology and XOR-dynamics in Boolean networks with varying input structure* (first arXiv submission 2008-09-09), analyse general XOR network dynamics and feedback dependence. Their matrix methods and general periodicity framework are prior knowledge. The contribution here is the wheel-specific **all-circumference** closed rank sequence, discontinuous two-adic transient-depth law, binomial-size recurrent subspace classification, and exact periodic-point and basin census. In the inspected material these specific wheel formulas were not stated. The use of general linear-algebra tools alone does not assert a new generic method.

## Limitations

This theorem applies to the unweighted open-neighbour XOR rule over \(\mathbb F_2\) and the stated wheel graphs; it does not establish corresponding laws for threshold, closed-neighbour, asynchronous, or higher-alphabet updates. The cycle formula expresses counts through explicit polynomial gcds rather than uniformly simplifying the primitive periods to a short list. Originality is assessed against accessible primary literature and indexed results; an unindexed equivalent may exist. No independent external mathematical audit has been performed.

## References

1. K. Sutner, *Additive Automata on Graphs*, Complex Systems **2** (1988), 649–661. Full text: https://content.wolfram.com/uploads/sites/13/2018/02/02-6-3.pdf.
2. L. Ciandrini, C. Maffi, A. Motta, B. Bassetti, M. Cosentino Lagomarsino, *Feedback topology and XOR-dynamics in Boolean networks with varying input structure*, arXiv:0809.1526, first submitted 2008-09-09, https://arxiv.org/abs/0809.1526.

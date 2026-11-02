# Exact one-node controllability ranks for rationally detuned ladder networks

## Finding

**Theorem (complete one-input rank law).** For every integer \(n\ge2\), take a two-rail ladder with \(n\) rungs, unit conductance on each longitudinal rail edge, and a common rational rung conductance \(r\ge1\). For a scalar input acting at position \(s\in\{1,\ldots,n\}\) on either rail, put \(g=\gcd(n,2s-1)\) and \(N=2n\). The Kalman controllability rank of the Laplacian system is exactly

\[
\operatorname{rank}\bigl[b,L_rb,\ldots,L_r^{N-1}b\bigr]
=2n-(g-1)-\delta_r(n,s),
\]

where

\[
\delta_r(n,s)=
\begin{cases}
\mathbf 1_{2\mid n}+\mathbf 1_{3\mid n\,\land\,3\nmid(2s-1)},&r=1,\\
\mathbf 1_{3\mid n},&r=3/2,\\
0,&r\in\mathbb Q,\ r\ge1,\ r\notin\{1,3/2\}.
\end{cases}
\]

In particular, a corner input is completely controllable for **every** \(n\ge2\) at the single fixed rational choice \(r=4/3\), and indeed at every rational \(r\ge1\) other than \(1\) or \(3/2\). The exceptional rung weights are sharp: at \(r=1\), an endpoint loses one dimension when \(2\mid n\) and one further dimension when \(3\mid n\); at \(r=3/2\), it loses one when \(3\mid n\).

## Assumptions and scope

The vertices are \((a,s)\), with rail \(a\in\{1,2\}\) and rung \(1\le s\le n\). Each edge joining adjacent positions on one rail has conductance \(1\); each rung has conductance \(r\). Let \(L_r\) denote the weighted combinatorial Laplacian, so that, in the vertex ordering induced by the product,

\[
L_r=L_{P_n}\otimes I_2+r I_n\otimes L_{P_2}.
\]

The dynamics are \(\dot z=-L_r z+b u\), with \(b\) the standard basis vector at a single vertex. The rank counts the full real state space, including the consensus mode. The complete classification is asserted for **rational** \(r\ge1\); it does not assert the same exception set for irrational or smaller positive rung strengths. Vertex position \(s\) means position along the path, not a graph label after arbitrary relabeling.

## Proof

**1. Spectral separation.** The path Laplacian has simple eigenvalues and nonzero eigenvectors with components

\[
\lambda_j=2-2\cos(\pi j/n),\qquad
v_j(s)=\cos\bigl(\pi j(s-1/2)/n\bigr),
\quad 0\le j<n.
\]

The two rung eigenvectors are the symmetric and antisymmetric rail vectors, with eigenvalues \(0\) and \(2r\). Consequently, every ladder eigenvalue belongs to one of the two simple-in-branch lists \(\lambda_j\) and \(\lambda_j+2r\). As the rail component of either rung eigenvector is nonzero at either rail, the only possible loss of a one-input mode comes from a zero of \(v_j(s)\) or from a cross-branch eigenvalue collision.

**2. Exact classification of rational collisions.** If \(\lambda_k=\lambda_j+2r\), necessarily \(0\le j<k<n\), and

\[
2r=2\cos(\pi j/n)-2\cos(\pi k/n).
\]

Each doubled cosine is an algebraic integer, hence so is their difference. Since \(2r\) is rational, it must be an integer. Also \(0<\lambda_k-\lambda_j<4\), so for \(r\ge1\) only \(2r=2\) or \(2r=3\) can occur.

For \(2r=2\), write \(x=2\cos(\pi j/n)\), \(y=2\cos(\pi k/n)=x-2\). Every algebraic conjugate of either doubled cosine is real and lies in \([-2,2]\). Thus every conjugate of the algebraic integer \(x-1\) lies in \([-1,1]\). **Elementary algebraic-integer lemma:** if all conjugates of an algebraic integer \(a\) lie in \([-1,1]\), then \(a\in\{-1,0,1\}\). Indeed, when \(a\ne0\), its nonzero integer field norm is a product of numbers of absolute value at most one, forcing each conjugate to have absolute value one; irreducibility then gives \(a=\pm1\). Hence \(x\in\{0,1,2\}\). The possibility \(x=0\) requires \(k=n\), excluded by \(k<n\). The other two possibilities give exactly

\[
(j,k)=(0,n/2)\quad(2\mid n),\qquad
(j,k)=(n/3,2n/3)\quad(3\mid n).
\]

For \(2r=3\), the same argument puts all conjugates of \(x-1\) in \([0,1]\); thus \(x\in\{1,2\}\). The first possibility forces \(k=n\) and is excluded. The second yields exactly \((j,k)=(0,2n/3)\), present iff \(3\mid n\). These are all possible rational cross-branch collisions at \(r\ge1\). Each has multiplicity two, and the two collisions at \(r=1\) occur at distinct eigenvalues.

**3. Vanishing path modes.** A path mode vanishes at position \(s\) precisely when

\[
\cos\bigl(\pi j(2s-1)/(2n)\bigr)=0,
\]

or equivalently \((2s-1)j/n\) is an odd integer. Write \(2s-1=g u\), \(n=g v\), with \(\gcd(u,v)=1\). Here \(u\) and \(g\) are odd. Necessarily \(j=v t\) with \(1\le t<g\) odd, so there are exactly \((g-1)/2\) zero modes. In the absence of a collision each zero mode removes two eigenvector directions, one from each branch, hence a loss of \(g-1\) dimensions.

**4. Accounting for collisions without double counting.** With one scalar input, a simple eigenspace contributes rank one exactly when its normalized eigenvector has nonzero input component. A repeated two-dimensional eigenspace contributes rank one when at least one of the two branch components is nonzero, and zero otherwise. Thus an extra rank loss of one occurs at a cross-branch collision **only if both branch path components are nonzero**; a zero in one component was already counted in step 3.

At \(r=1\), the pair \((0,n/2)\) has no zero components, adding \(\mathbf1_{2\mid n}\). For \((n/3,2n/3)\), \(v_{2n/3}(s)=\cos(\pi(2s-1)/3)\ne0\) at every integer \(s\), whereas \(v_{n/3}(s)=\cos(\pi(2s-1)/6)=0\) exactly when \(3\mid(2s-1)\). This adds \(\mathbf1_{3\mid n\,\land\,3\nmid(2s-1)}\). At \(r=3/2\), the pair \((0,2n/3)\) always has nonzero components, adding \(\mathbf1_{3\mid n}\). This proves the rank formula. Rail exchange is an automorphism, so both choices of rail have the same rank. A sign change from \(L_r\) to \(-L_r\) does not affect the Krylov span.

## Verification

The supplied `verify.py` builds the scaled integer Laplacian and computes actual Krylov ranks by Gaussian elimination over the prime field of order \(1{,}000{,}003\). It compares these with the formula at \(n=2,\ldots,20\), seven rational rung strengths \(1,3/2,4/3,5/2,7/4,2,9/7\), and representative boundary and interior vertices. It reports **504 matching rank cases**. These finite-field checks are independent computational tests; the all-size and characteristic-zero claims follow from the preceding proof, not from enumeration.

For reproducibility, run `python verify.py` with a Python 3 environment containing NumPy. The expected output begins with `PASS 504`.

## Relationship to prior work

Notarstefano and Parlangeli (arXiv:1203.0129v1, first posted 2012-03-01) study controllability and observability for ordinary **unweighted** Cartesian grid graphs. In particular, the \(r=1\) specialization falls within that established framework and is **not claimed as novel**. Their analysis uses path eigenspaces and multiplicities, but it does not provide the above exact arithmetic rank law for rational rung detuning \(r>1\). Parlangeli and Notarstefano (arXiv:1109.3556v1) establish the underlying path and cycle spectral/controllability theory; the path-zero count is a known component. The additional result here is the complete rational-coupling resonance classification together with the all-position rank formula and the universal all-length controllable tuning \(r=4/3\).

## Limitations

The theorem assumes a common rung conductance and unit rail conductances. A variable rung profile, arbitrary irrational coupling, multiple actuators and stronger requirements such as bounded control energy are not classified. Rank does not by itself quantify controllability Gramian conditioning. The literature comparison is not an exhaustive historical search, and an independent mathematical audit has not been performed.

## References

1. G. Notarstefano and G. Parlangeli, *Controllability and observability of grid graphs via reduction and symmetries*, arXiv:1203.0129v1 (2012-03-01), https://arxiv.org/abs/1203.0129 .
2. G. Parlangeli and G. Notarstefano, *On the reachability and observability of path and cycle graphs*, arXiv:1109.3556v1 (2011-09-16), https://arxiv.org/abs/1109.3556 .

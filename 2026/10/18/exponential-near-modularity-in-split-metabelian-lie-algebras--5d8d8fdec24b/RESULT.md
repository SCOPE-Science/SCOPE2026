# Exponential near-modularity in split metabelian Lie algebras

## Finding
Let \(q\) be any prime power. For pairwise distinct scalars \(\lambda_1,\ldots,\lambda_r\in\mathbb F_q\), \(2\le r\le q\), and integers \(a_1,\ldots,a_r\ge2\), put \(n=\sum_j a_j\) and form the \((n+1)\)-dimensional Lie algebra
\[
L=\mathbb F_q h\ltimes_T V,\quad V=\bigoplus_{j=1}^rV_j,\quad \dim V_j=a_j,\quad [h,v]=Tv,\quad T|_{V_j}=\lambda_j I.
\]
For its set \(\mathcal S(L)\) of **all** Lie subalgebras (including zero and \(L\)), let
\[
\operatorname{sd}(L)=\frac{\#\{(A,B)\in\mathcal S(L)^2:[A,B]\subseteq A+B\}}{|\mathcal S(L)|^2}.
\]
**The sharp multiplicity law**, with constants depending only on \(q\) and uniform in \(r\) and the multiplicities, is
\[
\boxed{1-\operatorname{sd}(L)=\Theta_q\left(q^{\frac12(n-\sum_{i<j}a_ia_j)}\right).}
\]
In particular, these algebras are nonmodular, yet their subalgebra commutativity degree tends to one whenever \(\min_j a_j\to\infty\) with \(q\) fixed. The rate is independent of the *values* of the distinct eigenvalues, depending on their multiplicities only.

An exact finite formula valid for every parameter in this domain is as follows. Put \(\mathcal I=\{X=\bigoplus_jX_j:X_j\le V_j\}\), \(x=\dim X\), \(X_j=X\cap V_j\), and \(\mathcal I_X\) for the lattice of \(T\)-invariant subspaces of \(V/X\). Write \({m\brack k}_q\) for a Gaussian binomial coefficient and
\[
H_q(x,z)=\sum_{t=0}^{x}{x\brack t}_q q^{z(x-t)}.
\]
Define the following **finite** integers:
\[
\begin{aligned}
N_0&=\sum_{k=0}^{n}{n\brack k}_q,\\
N_1&=\sum_{X\in\mathcal I}q^{n-\dim X}=q^n\prod_{j=1}^r\left(\sum_{k=0}^{a_j}{a_j\brack k}_q q^{-k}\right),\\
Q_{01}&=\sum_{X\in\mathcal I}q^{n-\dim X}\sum_{Z\in\mathcal I_X}H_q(\dim X,\dim Z),\\
Q_{11}&=\sum_{X,Y\in\mathcal I}q^{n-\dim(X\cap Y)}\left(1+\sum_{j=1}^r\big(q^{a_j-\dim(X_j+Y_j)}-1\big)\right).
\end{aligned}
\]
Then
\[
\boxed{\operatorname{sd}(L)=\frac{N_0^2+2Q_{01}+Q_{11}}{(N_0+N_1)^2}.}
\]
Every lattice in this expression is a direct product of ordinary finite-field subspace lattices, making the formula explicit using Gaussian binomial sums and intersection multiplicities.

## Assumptions and scope
The field can have any characteristic, including two; \(T\) is semisimple with at least two **distinct** field-rational eigenvalues, and each eigenspace has dimension at least two. The Lie algebra is metabelian and its nilradical contains \(V\). All probability statements use uniformly and independently chosen **Lie subalgebras**, not uniformly chosen vectors or matrices. The implicit positive constants in \(\Theta_q\) depend solely on fixed \(q\); the claim is not a field-size-uniform asymptotic. The exact finite formula also makes sense outside the minimum multiplicity restriction, but the claimed sharp multiplicity law is asserted only on the stated domain.

## Proof
**1. Classification.** A subalgebra contained in \(V\) is an arbitrary vector subspace: these are type zero. If a subalgebra \(A\) is not contained in \(V\), let \(X=A\cap V\). Then \(A=X+\langle h+v\rangle\) for a unique coset \(v+X\in V/X\). Closure is equivalent to \(TX\subseteq X\). Distinctness of the eigenvalues makes every invariant subspace exactly \(X=\bigoplus_j X_j\), since spectral projections are polynomials in \(T\). Consequently, there are \(N_0\) type-zero and \(N_1\) type-one subalgebras.

**2. Two type-zero subalgebras.** They always permute: their sum lies in the abelian ideal \(V\). This contributes \(N_0^2\) ordered pairs.

**3. One of each type.** For \(A=X+\langle h+v\rangle\) and \(W\le V\), the sum is a Lie subalgebra exactly when \(T(W)\subseteq W+X\), or, equivalently, \((W+X)/X\) is an invariant subspace \(Z\) of \(V/X\). If \(\dim X=x\) and \(\dim Z=z\), choose \(U=W\cap X\) of dimension \(t\) in \({x\brack t}_q\) ways. Then \(W/U\) is the graph of one of \(q^{z(x-t)}\) maps \(Z\to X/U\). Summing over \(t\) gives \(H_q(x,z)\); there are \(q^{n-x}\) possible lifts \(A\). The two orientations therefore contribute \(2Q_{01}\).

**4. Two type-one subalgebras.** Write \(A=X+\langle h+v\rangle\), \(B=Y+\langle h+w\rangle\) with invariant \(X,Y\), and \(Z=X+Y\). Their vector-space sum is \(Z+\langle h+v,w-v\rangle\). It is a Lie subalgebra if and only if the image \(\delta=(w-v)+Z\in V/Z\) spans an invariant line or is zero. Since the induced operator has distinct eigenspaces \(V_j/(X_j+Y_j)\), the number of valid \(\delta\) equals
\[
1+\sum_j\left(q^{a_j-\dim(X_j+Y_j)}-1\right).
\]
The surjective difference map \((V/X)\times(V/Y)\to V/Z\) has every fibre of size \(q^{n-\dim(X\cap Y)}\). This gives \(Q_{11}\). Combining all three types proves the exact formula.

**5. Upper asymptotic bound.** For fixed \(q\), Gaussian coefficients satisfy uniform two-sided bounds \({m\brack k}_q=\Theta_q(q^{k(m-k)})\). Completing squares in the sums yields
\[
N_0=\Theta_q(q^{n^2/4}),\qquad
N_1=\Theta_q\left(q^{n+\sum_j(a_j-1)^2/4}\right).
\]
These estimates have constants depending only on \(q\) because \(r\le q\). Hence, putting \(S=\sum_{i<j}a_ia_j\),
\[
\frac{N_1}{N_0}=\Theta_q\left(q^{(n-S)/2}\right).
\]
Since all \(a_j\ge2\), \(S\ge n\), so this ratio is bounded uniformly. Every nonpermuting ordered pair has at least one type-one member. Therefore
\[
1-\operatorname{sd}(L)\le\frac{2N_0N_1+N_1^2}{(N_0+N_1)^2}
=O_q\left(q^{(n-S)/2}\right).
\]

**6. Matching lower bound.** Choose invariant \(X=\bigoplus X_j\) with \(\dim X_j=\lfloor a_j/2\rfloor\). Let \(x=\dim X\), \(d=n-x\), so \(x=n/2+O_q(1)\), \(d=n/2+O_q(1)\), and \(dx=n^2/4+O_q(1)\). There are \(\Theta_q(q^{\sum_j a_j^2/4})\) such \(X\), each with \(q^d\) type-one lifts. Of the hyperplanes of \(V/X\), a positive \(q\)-dependent proportion are **not** invariant: indeed, separating one eigenspace of dimension \(u\ge1\) from the remaining eigenspaces of combined dimension \(v\ge1\) already yields
\[
\frac{(q^u-1)(q^v-1)}{q-1}
\]
noninvariant hyperplanes. For each such hyperplane \(Z\), choose a line \(U\le X\) and then a graph map \(Z\to X/U\). The resulting type-zero subspaces \(W\) have \(\dim W=d\), \(W\cap X=U\), and \((W+X)/X=Z\), so they do **not** permute with the corresponding type-one subalgebra. For each \(X\) the number of such \(W\) is \(\Theta_q(q^{dx-1})\). Therefore the number of nonpermuting ordered pairs is at least
\[
\Omega_q\left(q^{\sum_j a_j^2/4+d+dx}\right).
\]
Dividing by \((N_0+N_1)^2=\Theta_q(q^{n^2/2})\) yields the matching bound \(\Omega_q(q^{(n-S)/2})\). This also proves nonmodularity for every admissible parameter choice. Finally, if \(\min_j a_j\to\infty\) while \(q\) stays fixed, \(S-n\to\infty\), so \(\operatorname{sd}(L)\to1\).

## Verification
The accompanying `verify.py` constructs all subspaces by reduced row-echelon matrices over the prime fields of orders two and three. It independently selects Lie subalgebras by bracket closure, checks every ordered pair, and agrees with the finite formula for six configurations, including \((a_1,a_2)=(2,2)\) over \(\mathbb F_2\) and three distinct eigenvalues with unit multiplicities over \(\mathbb F_3\). The companion `independent.py` separately constructs every invariant subspace for block sizes \((2,2,2)\) over \(\mathbb F_3\) and \((2,2)\) over \(\mathbb F_2\), reproducing the pair sums from explicit intersection dimensions. Run both scripts with Python 3 from their common directory. The general result is proved above; finite cases do not establish the asymptotic.

## Relationship to prior work
Muhie, Otera and Russo (2026, arXiv:2609.19086) introduce the subalgebra commutativity degree, establish general bounds, and calculate special Heisenberg and three-dimensional simple Lie-algebra cases. Classical modularity theory gives degree one for genuinely scalar-action almost-abelian Lie algebras; that scalar case is **not** part of this theorem. A previously computed four-dimensional two-eigenvalue case with eigenspace multiplicities \((2,1)\) is outside the present minimum-multiplicity scope, and the exact formula agrees with that case if evaluated there. The new result is the uniform arbitrary split-spectrum pair enumeration together with the sharp multiplicity-dependent exponential law; neither follows as a special case or numerical substitution of those limited-dimensional findings.

## Limitations
Only semisimple operators with pairwise distinct eigenvalues in the ground field are covered. Jordan blocks, nonsplit irreducible blocks, and repeated eigenvalues not grouped into eigenspaces require different subalgebra descriptions. The asymptotic is fixed-field and does not assert a universal constant or a limit when \(q\) varies. Independent verification has not been performed; the computations described above are finite tests rather than infinite certificates. An implicit formulation in less accessible prior literature is a remaining bibliographic risk.

## References
- S. K. Muhie, D. E. Otera, F. G. Russo, *On the number of modular pairs in finite dimensional Lie algebras on finite fields*, first publicly posted September 16, 2026, arXiv:2609.19086, https://arxiv.org/abs/2609.19086.
- O. Kolman, *Semi-modular Lie algebras*, 1965, as cited and discussed in Muhie--Otera--Russo, Section 2. Their scalar-action modularity result is background, not claimed here.
- *Plane counts control subalgebra commutativity in dimension three*, public indexed mathematical result, record identifier 0c4c7f02cc9c; the dimension-three scope does not give the high-multiplicity theorem.

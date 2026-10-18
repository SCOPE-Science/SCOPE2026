# A sharp irreducibility transition for commuting minimal-nilpotent matrix tuples

## Finding

Let \(k\) be an algebraically closed field, \(n\ge4\), and \(r\ge1\). Write \(V=k^n\) and define the minimal-nilpotent orbit closure
\[
\mathcal R_n=\{A\in\operatorname{End}(V):\operatorname{rank}A\le1,\ A^2=0\}.
\]
Let \(\mathcal C_{n,r}\) be the **reduced** algebraic variety of ordered tuples \((A_1,\ldots,A_r)\in\mathcal R_n^r\) that commute pairwise. For \(1\le d<n\), put
\[
\mathcal X_d=\{(A_i)\in\mathcal C_{n,r}:\text{there exists }U\le V,\ \dim U=d,\ A_i(V)\subseteq U\subseteq\ker A_i\ \forall i\}.
\]
These are closed irreducible subvarieties. Their irreducible-component structure is **exactly**:

- If \(n\ge2r\), then \(\mathcal C_{n,r}=\mathcal X_r\) is irreducible, of dimension \(r(2n-r-1)\).
- If \(n<2r\), its irreducible components are precisely \(\mathcal X_d\) for
\[
\max(1,n-r)\le d\le\min(r,n-1).
\]
Each such component has dimension \(d(n-d)+r(n-1)\). In particular \(\mathcal C_{n,r}\) is irreducible **if and only if** \(n\ge2r\).

The dimension of the entire variety is
\[
\dim\mathcal C_{n,r}=
 r(n-1)+\begin{cases}
 r(n-r),&n\ge2r,\\
 \lfloor n^2/4\rfloor,&n<2r.
 \end{cases}
\]
The components need not be equidimensional: at \((n,r)=(4,3)\), the three components have dimensions \(12,13,12\).

There is also an exact **all-arity finite-field census**. For every prime power \(q\), define \(N_{n,r}(q)\) as the number of commuting ordered \(r\)-tuples in \(\mathcal R_n(\mathbb F_q)\). Then
\[
\boxed{
N_{n,r}(q)=\sum_{d=0}^{n}{n\brack d}_q
 \sum_{t=0}^{d}(-1)^{d-t}q^{\binom{d-t}{2}}
 {d\brack t}_q\left(1+\frac{(q^t-1)(q^{n-d}-1)}{q-1}\right)^r.
}
\]
Here \({a\brack b}_q\) is the Gaussian binomial coefficient. For example \(N_{4,2}(2)=2836\) and \(N_{4,3}(2)=38536\).

## Assumptions and scope

All geometric assertions concern the reduced zero set over an **algebraically closed field of arbitrary characteristic**. They do not assert reducedness of any naive commutator-equation scheme. The set \(\mathcal R_n\) includes the zero matrix; nonzero elements have rank one and nilpotency index two. Tuples are ordered and individual entries may be zero or equal. The geometric theorem is asserted for every integer \(n\ge4\), \(r\ge1\). The point-count theorem holds over every \(\mathbb F_q\), with no characteristic restriction. The earlier low-dimensional case \(n=3\) is deliberately not claimed as original.

## Proof

**1. Commutation collapses to annihilation.** Let \(A,B\in\mathcal R_n\) with \(AB=BA\). If their common product is nonzero, then its one-dimensional image equals both \(\operatorname{im}A\) and \(\operatorname{im}B\). But both \(A\) and \(B\) kill this common image line because \(A^2=B^2=0\); hence \(AB=0\), a contradiction. Thus \(AB=BA=0\). The converse is immediate. Since every individual matrix squares to zero, every tuple in \(\mathcal C_{n,r}\) satisfies \(A_iA_j=0\) for **all** indices \(i,j\).

**2. Common image and kernel.** Put
\[
S=\sum_i\operatorname{im}A_i,\qquad K=\bigcap_i\ker A_i,
\qquad a=\dim S,\quad b=\operatorname{codim}K.
\]
Mutual annihilation gives \(S\subseteq K\). Since every \(A_i\) has rank at most one, \(a,b\le r\). If \(n\ge2r\), then \(a\le r\le n-b\), so there exists an \(r\)-dimensional subspace \(U\) with \(S\subseteq U\subseteq K\); hence \(\mathcal C_{n,r}=\mathcal X_r\). If \(n<2r\), there is at least one integer \(d\) in the displayed component-index interval satisfying \(a\le d\le n-b\). Choosing \(U\) of this dimension shows that the union of the indicated \(\mathcal X_d\)'s equals \(\mathcal C_{n,r}\).

**3. Closedness and irreducibility of each candidate.** Consider the incidence space over \(\operatorname{Gr}(d,V)\) of a subspace \(U\) and an ordered tuple of rank-at-most-one maps \(V/U\to U\). Locally on the Grassmannian, the fiber is the \(r\)-fold product of the determinantal rank-at-most-one cone in \(\operatorname{Hom}(k^{n-d},k^d)\). This cone is irreducible (the image of \(k^d\times(k^{n-d})^*\) under the outer-product map), of dimension \(n-1\). The incidence space is irreducible. Its image under the projection to tuples is exactly \(\mathcal X_d\). The incidence projection is closed because it is the restriction of the projection from an affine space times the projective Grassmannian; therefore \(\mathcal X_d\) is closed and irreducible.

**4. Dimension and noncontainment.** For every retained component index one has \(r\ge d\). When \(n<2r\), one also has \(r\ge n-d\); the latter inequality is unnecessary for the sole index \(d=r\) when \(n\ge2r\). In the incidence fiber, a nonempty open set of tuples has images spanning \(U\) whenever \(r\ge d\), so its intermediate subspace \(U\) is uniquely recovered as the sum of the images. Thus the incidence projection is generically one-to-one for every retained \(d\), giving
\[
\dim\mathcal X_d=d(n-d)+r(n-1).
\]
When \(n<2r\), a further nonempty open set has the dual functionals spanning \((V/U)^*\). On that open set, the common kernel is also exactly \(U\). If a tuple in this open set belonged to some \(\mathcal X_e\), the condition on its image forces \(e\ge d\), while the condition on its kernel forces \(e\le d\), so \(e=d\). Therefore no retained \(\mathcal X_d\) lies inside a distinct retained \(\mathcal X_e\). Since these finitely many closed irreducible varieties cover \(\mathcal C_{n,r}\), they are precisely its irreducible components. For \(n\ge2r\) the sole component is \(\mathcal X_r\). Maximizing \(d(n-d)\) over the indicated interval gives the dimension formula.

**5. Finite-field counting.** Fix an \(\mathbb F_q\)-subspace \(U\) of dimension \(d\) and another subspace \(W\le U\) of dimension \(t\). The rank-at-most-one maps \(V/U\to W\) number
\[
1+\frac{(q^t-1)(q^{n-d}-1)}{q-1},
\]
because each nonzero map is an outer product of two nonzero vectors, modulo the free scalar action of \(\mathbb F_q^\times\). Raising this expression to the \(r\)-th power counts ordered tuples whose images lie in \(W\) and whose kernels all contain \(U\). Subspace-lattice Möbius inversion, using \(\mu(W,U)=(-1)^{d-t}q^{\binom{d-t}{2}}\), counts tuples whose **sum of images is exactly \(U\)**. Summing over the \({n\brack d}_q\) choices of \(U\) gives the stated formula. The zero tuple occurs once in the \(d=0\) contribution. Every nonzero tuple has a unique image span, so there is no overcount.

## Verification

Run `python3 verify_rank_one.py` using Python 3 and the standard library only. The script constructs every matrix in the rank-one nilpotent cone for the listed test configurations by outer products, independently multiplies the resulting matrices, verifies that commutation is equivalent to mutual annihilation, and exhaustively counts ordered commuting tuples using neighbor-bitset recursion. It independently evaluates the Gaussian-binomial formula. It also checks the candidate component-index and dimension expressions for every \(2\le n\le15\), \(1\le r\le15\). Exhaustive matrix computations include \((n,r,q)=(4,2,2),(4,3,2),(3,4,2),(3,2,4)\) and nine other configurations. The script prints `VERIFY_OK_MINIMAL_NILPOTENT_TUPLES` if all tests pass. These are finite corroborations only; the proof covers all fields and parameters in scope.

## Relationship to prior work

The nilpotent commuting-variety literature studies all nilpotent matrices, whereas this theorem restricts **every entry to the minimal nonzero nilpotent orbit closure**. Ngo's 2013 paper explicitly treats the corresponding \(3\times3\) subregular/minimal-orbit closure and its reducibility: that case is an antecedent, not a novelty claim. Guralnick–Ngo (2013) and Ngo (2014) address reducibility and dimensions for substantially larger nilpotent commuting varieties; their stated conclusions do not imply the precise rank-one component list or point-count formula for arbitrary \(n\ge4\). Huang (2021) enumerates mutually annihilating **pairs of unrestricted matrices**; that is relevant to the two-entry boundary but does not give the all-arity rank-one component theorem. Levy–Ngo–Šivic (2022) determine maximal-dimensional components of the unrestricted nilpotent commuting variety for sufficiently long tuples, not the reduced minimal-orbit subvariety. No claim is made of exhaustive bibliographic priority, and a specialized result formulated as a rank-constrained representation variety could overlap this theorem.

## Limitations

The scheme structure of the equations is not classified; nilpotent embedded components, singularities and normality are not determined. The component list concerns the rank-at-most-one nilpotent locus only, not all square-zero matrices or the unrestricted nilpotent commuting variety. Conjugacy orbits of tuples and moduli quotients are not counted. The precise earlier \(n=3\) antecedent is excluded from the claimed original scope. Independent verification and exhaustive literature-priority checks have not been performed.

## References

- N. V. Ngo, *Mixed Commuting Varieties over Simple Lie Algebras*, arXiv:1301.2712 (first publicly posted 12 January 2013), especially Section 4 and Lemma 4.4.2. https://arxiv.org/abs/1301.2712
- R. M. Guralnick and N. V. Ngo, *Reducibility of Nilpotent Commuting Varieties*, arXiv:1308.2420 (11 August 2013), especially Section 3.4. https://arxiv.org/abs/1308.2420
- N. V. Ngo, *On Nilpotent Commuting Varieties and Cohomology of Frobenius Kernels*, arXiv:1401.6820 (27 January 2014), especially Section 3. https://arxiv.org/abs/1401.6820
- Y. Huang, *Mutually Annihilating Matrices, and a Cohen–Lenstra Series for the Nodal Singularity*, arXiv:2110.15566 (29 October 2021), Theorem 1.2. https://arxiv.org/abs/2110.15566
- P. D. Levy, N. V. Ngo and K. Šivic, *Commuting Varieties and Cohomological Complexity Theory*, arXiv:2105.07918 (17 May 2021), Sections 1 and 4. https://arxiv.org/abs/2105.07918

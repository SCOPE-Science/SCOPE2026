# All group Rota–Baxter operators on higher finite Heisenberg groups

## Finding

Let \(p\) be an odd prime and \(n\geq 2\). On the \(2n\)-dimensional vector space \(V=\mathbb F_p^{2n}\), fix a nondegenerate alternating form \(\omega\), and give \(H=V\times\mathbb F_p\) the group law
\[
(v,z)(w,t)=(v+w,z+t+\tfrac12\omega(v,w)).
\]
A **group Rota–Baxter operator** is a set map \(B:H\to H\) such that
\[
B(g)B(h)=B(gB(g)hB(g)^{-1})\quad(g,h\in H).
\]
**Classification.** Every such operator, uniquely, has the form
\[
 B(v,z)=\big(Tv,\;cz-\tfrac c2\omega(Tv,v)+\ell(v)\big),
\]
where \(c\in\mathbb F_p\), \(T\in\operatorname{End}_{\mathbb F_p}(V)\), and \(\ell\in V^*\), subject to the single condition
\[
 \omega((T-cI)v,(T-cI)w)=c(c+1)\omega(v,w)\qquad(v,w\in V).
\]
There are no additional constraints.

**Exact enumeration.** Put
\[
 I_{n,r}(p)=\frac{\prod_{i=0}^{r-1}(p^{2n-i}-p^i)}{\prod_{i=0}^{r-1}(p^r-p^i)}\quad(0\leq r\leq n),
 \qquad N_{n,p}=\sum_{r=0}^{n}I_{n,r}(p)\prod_{i=0}^{r-1}(p^{2n}-p^i),
\]
with empty products equal to one. Then the exact number of Rota–Baxter operators on \(H\) is
\[
 \boxed{p^{2n}\left(2N_{n,p}+(p-2)p^{n^2}\prod_{j=1}^{n}(p^{2j}-1)\right)}.
\]
More precisely, for each of the two scalar values \(c=0,-1\), and for every \(0\leq r\leq n\), the number of operators with \(\operatorname{rank}(T-cI)=r\) is
\[
 \boxed{p^{2n} I_{n,r}(p)\prod_{i=0}^{r-1}(p^{2n}-p^i)}.
\]
For each of the other \(p-2\) values of \(c\), there are exactly \(p^{2n}|\operatorname{Sp}_{2n}(p)|\) operators, where
\[
 |\operatorname{Sp}_{2n}(p)|=p^{n^2}\prod_{j=1}^{n}(p^{2j}-1).
\]
In particular, when \(n=2\) and \(p=3\), the exact number is \(45{,}152{,}802\).

## Assumptions and scope

The group is the standard exponent-\(p\), extraspecial Heisenberg group of order \(p^{2n+1}\). Here \(n\geq2\) and \(p\geq3\) is prime. The center is \(Z=\{(0,z):z\in\mathbb F_p\}\); inversion is \((v,z)^{-1}=(-v,-z)\), and conjugation is
\[
 (a,b)(v,z)(a,b)^{-1}=(v,z+\omega(a,v)).
\]
The result counts **labeled set maps** satisfying the displayed group identity, not conjugacy classes of maps. Every map is counted once by its unique triple \((c,T,\ell)\). No claim is made in characteristic two, nor for extraspecial groups of exponent \(p^2\).

## Proof

### 1. The center must map into the center

The defining identity with \(h=1\) yields \(B(1)=1\). For central \(z\in Z\), it also yields
\[
 B(gz)=B(g)B(z).
\]
Consequently, the restriction of \(B\) to \(Z\) is a homomorphism. Fix its standard generator \(z_0=(0,1)\), and write \(B(z_0)=b=(u,s)\). Then \(B(z_0^a)=b^a\) for all \(a\in\mathbb F_p\).

For \(g=(v,t)\), apply the identity instead with \(g=z_0\), \(h=g\). The commutator formula gives
\[
 b B(g)=B(z_0 bgb^{-1})=B(gz_0^{1+\omega(u,v)})
 =B(g)b^{1+\omega(u,v)}.
\]
Rearranging gives
\[
 bB(g)b^{-1}B(g)^{-1}=B(g)b^{\omega(u,v)}B(g)^{-1}.
\]
The left side lies in \(Z\), since \(H\) has nilpotence class two. Hence \(b^{\omega(u,v)}\in Z\). If \(u\ne0\), nondegeneracy supplies \(v\) for which \(\omega(u,v)\ne0\); because \(b\) has exponent dividing \(p\), this forces \(b\in Z\), a contradiction. Thus \(u=0\), and \(B(Z)\subseteq Z\). Write \(B(0,z)=(0,cz)\) for a unique \(c\in\mathbb F_p\).

### 2. Additivity of the noncentral coordinate

The center identity implies
\[
 B(v,z)=(b_0(v),cz+f(v))
\]
for functions \(b_0:V\to V\) and \(f:V\to\mathbb F_p\), with \(b_0(0)=0\) and \(f(0)=0\). Comparing \(V\)-coordinates in the Rota–Baxter identity for \((v,0)\) and \((w,0)\) shows
\[
 b_0(v+w)=b_0(v)+b_0(w).
\]
Because \(V\) is a vector space over the prime field, \(b_0=T\) for a unique \(\mathbb F_p\)-linear map \(T\).

### 3. The exact quadratic condition

Compare central coordinates in that same identity. Using the group law and the conjugation formula, one obtains for every \(v,w\in V\)
\[
 f(v+w)-f(v)-f(w)
 =\tfrac12\omega(Tv,Tw)-c\omega(Tv,w)-\tfrac c2\omega(v,w).\tag{1}
\]
The left side is symmetric in \(v,w\). Subtracting the right side with swapped arguments gives the necessary and sufficient alternating-form relation
\[
 \omega(Tv,Tw)=c\big(\omega(Tv,w)+\omega(v,Tw)+\omega(v,w)\big),\tag{2}
\]
which is equivalent, by expansion, to
\[
 \omega((T-cI)v,(T-cI)w)=c(c+1)\omega(v,w).\tag{3}
\]
Under (2), the right side of (1) becomes
\[
 -\tfrac c2\big(\omega(Tv,w)+\omega(Tw,v)\big).
\]
It is precisely the additive polarization of \(q(v)=-\tfrac c2\omega(Tv,v)\). Hence \(f-q\) is additive, and therefore equals a unique \(\ell\in V^*\). Conversely, if (3) holds, this expression for \(f\) satisfies (1), and direct substitution into the group identity proves that \(B\) is a Rota–Baxter operator. This establishes both classification and uniqueness.

### 4. Exact arithmetic strata

Put \(U=T-cI\). If \(c\notin\{0,-1\}\), equation (3) makes \(U\) a symplectic similitude with fixed nonzero multiplier \(c(c+1)\). A fixed nonzero multiplier occurs: in a symplectic basis, multiply one Lagrangian summand by that multiplier and fix its dual summand. The set of maps of that multiplier is a single coset of \(\operatorname{Sp}_{2n}(p)\), of cardinality \(p^{n^2}\prod_{j=1}^n(p^{2j}-1)\).

If \(c\in\{0,-1\}\), equation (3) says exactly that the image of \(U\) is totally isotropic. Its possible rank is \(0\leq r\leq n\). For a prescribed isotropic image \(W\) of dimension \(r\), the number of surjective \(\mathbb F_p\)-linear maps \(V\to W\) is
\[
 \prod_{i=0}^{r-1}(p^{2n}-p^i).
\]
To count choices of \(W\), choose an ordered basis of an isotropic subspace. At stage \(i\), the next vector lies in an orthogonal complement of dimension \(2n-i\), but outside the \(p^i\)-element span of preceding vectors, giving \(p^{2n-i}-p^i\) choices. Dividing the resulting product by the number \(\prod_{i=0}^{r-1}(p^r-p^i)\) of ordered bases of \(\mathbb F_p^r\) gives \(I_{n,r}(p)\). Finally, each admissible \((c,T)\) admits all \(|V^*|=p^{2n}\) choices of \(\ell\). Multiplication and summation prove all enumerations.

## Verification

The standalone source file `verify.py` checks the defining group identity against the matrix criterion independently. For \(p=3\) in dimension two it enumerates all matrices and tests every group-element pair; it also tests random independent linear functionals. Complete dimension-two matrix counts are checked for \(p=3,5,7\); dimension-four random tests include all scalar strata; finite-product counting formulas are evaluated for \(n=1,2,3\). The concluding message is `VERIFY_OK`. The code's dimension-two and random checks do not establish the theorem for all dimensions; steps 1–4 above do.

The formula gives \(N_{2,3}=252{,}801\), \(|\operatorname{Sp}_4(3)|=51{,}840\), and \(3^4(2\cdot252{,}801+51{,}840)=45{,}152{,}802\). The dimension-two case is used only to test the general formula, not as a claim of priority over known order-\(p^3\) classifications.

## Relationship to prior work

Savelyev's 2026 classification of Rota–Baxter operators on extraspecial groups (arXiv:2608.28291) proves center preservation for all extraspecial groups and explicitly classifies the two nonabelian groups of order \(p^3\). Its general class-two construction concerns automorphism-based operators. It does not state the complete all-operator enumeration and isotropic-rank strata for the standard groups of order \(p^{2n+1}\) with \(n\geq2\). The present proof independently establishes center preservation for this group and includes the generally noninvertible regimes.

Rathee's 2024 work (arXiv:2402.15428) studies Rota–Baxter operators and braces over a three-dimensional Heisenberg Lie group. Its Lie/group constructions are relevant background, but the finite, higher-rank all-map count and rank distribution above are not directly among its results. Bardakov and Gubarev's theory of Rota–Baxter groups and skew braces provides structural context, not the displayed finite high-rank census. A possibly equivalent formulation in older high-dimensional Lie-operator or finite symplectic-geometry literature remains a historical-priority risk; the claim of novelty is qualified accordingly.

## Limitations

The classification is for the specific exponent-\(p\) standard extraspecial Heisenberg group, over an odd prime field, and does not determine conjugacy classes under automorphisms or cover arbitrary extraspecial groups of exponent \(p^2\). It determines finite counts symbolically but does not settle the classification of Rota–Baxter maps on all nilpotent groups. The self-review is not independent validation; full historical priority requires further scholarly confirmation.

## References

1. A. Savelyev, *Rota—Baxter operators on extraspecial groups*, arXiv:2608.28291 (first posted 2026-08-28), https://arxiv.org/abs/2608.28291.
2. N. Rathee, *Rota--Baxter operators and skew left brace structures over Heisenberg Group*, arXiv:2402.15428 (2024), https://arxiv.org/abs/2402.15428.
3. V. G. Bardakov and V. Gubarev, *Rota–Baxter groups, skew left braces, and the Yang–Baxter equation*, Journal of Algebra 596 (2022), 328–351, https://doi.org/10.1016/j.jalgebra.2021.12.036.

# Sharp rank eight for banded \(\mu_2\)-gerbes over nonorientable five-manifolds

## Finding

**Theorem.** Let \(B\) vary over connected closed nonorientable smooth five-manifolds and let \(\mathcal G\to B\) vary over smooth banded \(\mu_2\)-gerbes. The possible minimum positive complex regular-bundle ranks are exactly
\[
\bigl\{r_{\min}(\mathcal G)\bigr\}=\{2,4,8\}.
\]
In particular the bound eight of Becerra--Lupercio, Proposition 7.6, is sharp in the stated constant-isotropy category. An explicit rank-eight example is the gerbe over the mapping torus of
\[
f:S^2\times S^2\longrightarrow S^2\times S^2,\qquad f(x,y)=(y,-x),
\]
whose gerbe class restricts to the sum of the mod-two fundamental cohomology classes in degree two of the two sphere factors.

## Assumptions and scope

Here a smooth banded \(\mu_2\)-gerbe means a smooth orbifold stack locally of the form \(U\times B\mu_2\), with trivially acting and consistently identified stabilizer \(\mu_2\) at every point. Its banding class is \(\xi\in H^2(B;\mathbb Z/2)\), with associated torsion Brauer class \(\alpha=\beta_2(\xi)\in H^3(B;\mathbb Z)\). A positive-rank complex bundle is *regular* when every fiber representation of \(\mu_2\) is a positive multiple of \(\mathbb C[\mu_2]\). Let \(r_{\min}\) be the least possible such rank.

All manifolds here are connected, smooth, compact, five-dimensional, and without boundary. The claimed sharp bound concerns gerbes with **constant ineffective** stabilizer \(\mu_2\), not orbifolds admitting both trivial and nontrivial stabilizers.

## Proof

**1. Universal rank bound.** For a closed nonorientable connected five-manifold \(B\), integral Poincaré duality with orientation coefficients gives
\[
H^5(B;\mathbb Z)\cong H_0(B;\mathcal O_B)\cong\mathbb Z/2.
\]
When \(\alpha=0\), an odd line bundle on the gerbe and a trivial line produce a regular bundle of rank two. For \(\alpha\) of period two, Antieau--Williams' Theorem A gives
\[
\operatorname{ind}(\alpha)
=2\operatorname{ord}\!\left(
\frac{\beta_4(P_2(\xi))+\alpha\smile H^2(B;\mathbb Z)}{\alpha\smile H^2(B;\mathbb Z)}
\right).
\]
Its obstruction lives in the quotient of \(H^5(B;\mathbb Z)\cong\mathbb Z/2\), so the order is at most two and \(\operatorname{ind}(\alpha)\) is either two or four. Becerra--Lupercio's Theorem 7.5 gives the **actual**, not merely stable, minimum rank
\[
r_{\min}(\mathcal G)=2\operatorname{ind}(\alpha)
\]
for any banded order-two gerbe over a finite five-complex. Thus the minimum belongs to \(\{2,4,8\}\). Smoothing does not change the regular rank or stabilizer representations; see their Proposition 7.6.

**2. A smooth nonorientable mapping torus.** Let \(F=S^2\times S^2\), and let \(a:S^2\to S^2\) be the antipodal map of degree \(-1\). Put \(f(x,y)=(y,a(x))\) and
\[
N=\bigl(F\times[0,1]\bigr)/\bigl((z,1)\sim(f(z),0)\bigr).
\]
The transposition of two even-dimensional sphere factors preserves the product orientation, while \(a\) reverses it, so \(f\) reverses orientation. Consequently \(N\) is a connected closed smooth **nonorientable** five-manifold.

Let \(u,v\in H^2(F;\mathbb Z)\) be pullbacks of the respective fundamental degree-two classes, normalized by \(\langle uv,[F]\rangle=1\). We have
\[
f^*u=v,\qquad f^*v=-u,\qquad f^*(uv)=-uv.
\]
In the ordered basis \((u,v)\), the degree-two monodromy matrix and its difference with the identity are
\[
A=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
A-I=\begin{pmatrix}-1&-1\\1&-1\end{pmatrix}.
\]
The latter has determinant two, has zero integral kernel, and has cokernel \(\mathbb Z/2\) (its entries have greatest common divisor one). Since \(H^1(F;\mathbb Z)=H^3(F;\mathbb Z)=0\), the integral mapping-torus (Wang) sequence yields
\[
H^2(N;\mathbb Z)=0,\quad
H^3(N;\mathbb Z)\cong\mathbb Z/2,\quad
H^4(N;\mathbb Z)=0,\quad
H^5(N;\mathbb Z)\cong\mathbb Z/2.
\]
The final two assertions use the multiplication-by-\(-1\) action on \(H^4(F;\mathbb Z)=\mathbb Z\).

**3. The degree-two gerbe class and its square.** Modulo two, \(A\) simply swaps \(\bar u\) and \(\bar v\). The mod-two Wang sequence (again using vanishing odd cohomology of \(F\)) gives an isomorphism from \(H^2(N;\mathbb Z/2)\) to the invariant line of \(H^2(F;\mathbb Z/2)\), spanned by \(\bar u+\bar v\). Let \(\xi\) be its unique nonzero class. Since \(H^2(N;\mathbb Z)=0\) and \(H^3(N;\mathbb Z)=\mathbb Z/2\), the coefficient-sequence Bockstein sends \(\xi\) to a generator
\[
\alpha=\beta_2(\xi)\ne0\in H^3(N;\mathbb Z).
\]
Its period is exactly two.

Now take coefficients \(\mathbb Z/4\). The monodromy on \(H^4(F;\mathbb Z/4)\cong\mathbb Z/4\) is multiplication by \(-1\). As \(H^3(F;\mathbb Z/4)=0\), the mapping-torus restriction embeds
\[
H^4(N;\mathbb Z/4)\hookrightarrow H^4(F;\mathbb Z/4)
\]
with image \(\ker(-1-1)=\{0,2\bar{u}\bar{v}\}\), a group of order two. The natural Pontryagin square \(P_2\) has the integral-lift property: if \(z\) is the reduction of integral degree-two class \(w\), then \(P_2(z)\) is the reduction modulo four of \(w^2\). Hence on \(F\), since \(u^2=v^2=0\),
\[
P_2(\xi)|_F=P_2(\bar u+\bar v)
=\rho_4\!\left((u+v)^2\right)=2uv\pmod4\ne0.
\]
Thus \(P_2(\xi)\) is the nonzero element of \(H^4(N;\mathbb Z/4)\). The coefficient Bockstein \(\beta_4:H^4(N;\mathbb Z/4)\to H^5(N;\mathbb Z)\) is **injective** because \(H^4(N;\mathbb Z)=0\). Therefore
\[
\beta_4(P_2(\xi))\ne0\in H^5(N;\mathbb Z)\cong\mathbb Z/2.
\]
Moreover \(\alpha\smile H^2(N;\mathbb Z)=0\), so this obstruction survives the quotient in Antieau--Williams' theorem with order exactly two.

**4. Exact index and regular rank.** Antieau--Williams' dimension-six formula now gives
\[
\operatorname{ind}(\alpha)=\operatorname{per}(\alpha)\cdot
\operatorname{ord}(\widetilde Q(\alpha))=2\cdot2=4.
\]
The class \(\xi\) defines a smooth banded \(\mu_2\)-gerbe \(\mathcal G_\xi\to N\), for example by a smooth good-cover Čech two-cocycle with values in the discrete group \(\mu_2\). Its weight-one twisted bundle must have rank divisible by four, so a regular bundle has rank divisible by eight. Conversely Becerra--Lupercio Theorem 7.5/Proposition 7.3 realizes the weight-one twisted index four by an actual complex rank-four bundle: in dimension five the condition \(2\cdot4\ge5-1\) holds. Adding an ordinary rank-four weight-zero bundle yields a smooth regular rank-eight bundle. Therefore \(r_{\min}(\mathcal G_\xi)=8\).

**5. Attainment of every possible minimum.** A trivial gerbe over any nonorientable closed five-manifold admits a regular rank-two bundle. For rank four, Becerra--Lupercio Theorem 9.2 constructs a smooth banded order-two gerbe \(\mathcal T\to T\) over a closed nonorientable three-dimensional mapping torus, with minimum rank four. On the nonorientable five-manifold \(T\times S^2\), the pulled-back gerbe has rank four; a rank-two bundle would restrict to a rank-two regular bundle on \(\mathcal T\), impossible. Together with the preceding construction this proves exactly the asserted set of minima.

## Verification

The accompanying standalone `proof_check.py` recomputes the integral Smith data for the degree-two monodromy, the modulo-two fixed vector, the modulo-four fixed subgroup in degree four, the coefficient Bockstein's domain and codomain orders, and the resulting index-to-rank arithmetic. Run `python3 proof_check.py`; the expected last line is `VERIFY_OK`. These small exact checks are not substitutes for the mapping-torus/Wang theorem, Pontryagin-square naturality, Poincaré duality, or the cited period--index and gerbe realization theorems; those are the mathematical proof's explicitly identified inputs.

## Relationship to prior work

Becerra--Lupercio's *Regular bundles on orbifolds II: ranks and obstructions* (arXiv:2610.02555v1), Proposition 7.6, proves an upper bound eight for banded order-two gerbes over closed nonorientable five-manifolds and **explicitly leaves its attainment open**. Their Theorem 7.5 gives the rank--index equality used here and Theorem 9.2 provides the rank-four example. Thus their results alone do not supply a manifold attaining eight. The new ingredient is the orientation-reversing \(S^2\times S^2\) monodromy and its nonzero integral secondary obstruction.

Antieau--Williams, *The topological period-index problem over 6-complexes* (arXiv:1208.4430), Theorem A, proves the general index formula. It does not construct this particular five-manifold. Crowley--Grant (arXiv:1802.01296v3) construct **six-dimensional** manifolds with period-two index-eight classes; their examples have different dimension and index, and neither supplies this closed nonorientable five-dimensional period-two index-four example. The proposed finding depends on these published foundations but is not the same statement nor an immediate specialization absent the monodromy and Pontryagin-square calculation.

## Limitations

The stabilizer is ineffective and of order two at **every** point, so the free locus is empty. No conclusion is claimed for closed nonorientable smooth five-orbifolds containing **both** trivial and order-two stabilizers; this is Becerra--Lupercio Question 10.2. No novelty or verification is asserted for arbitrary higher-degree gerbes, arbitrary nonconstant isotropy, or all closed five-dimensional orbifolds. An unindexed earlier equivalent mapping-torus construction cannot be excluded by search alone.

## References

1. E. Becerra and E. Lupercio, *Regular bundles on orbifolds II: ranks and obstructions*, arXiv:2610.02555v1, first made public 2026-10-01; especially Proposition 7.3, Theorem 7.5, Proposition 7.6, Theorem 9.2, and Questions 10.2. https://arxiv.org/html/2610.02555v1
2. B. Antieau and B. Williams, *The topological period-index problem over 6-complexes*, Journal of Topology 7 (2014), 617--640, Theorem A; arXiv:1208.4430. https://arxiv.org/pdf/1208.4430
3. D. Crowley and M. Grant, *The topological period-index conjecture for spin-c 6-manifolds*, Annals of K-Theory 5 (2020), 605--620; arXiv:1802.01296v3, especially Theorem 1.4. https://arxiv.org/pdf/1802.01296

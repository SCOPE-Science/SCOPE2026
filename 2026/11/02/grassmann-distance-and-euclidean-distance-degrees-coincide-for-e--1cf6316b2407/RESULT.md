# Grassmann distance and Euclidean distance degrees coincide for every rational-normal-scroll ruling curve

## Finding
Fix integers \(d\ge2\) and \(2\le n_1\le\cdots\le n_d\). Put \(m=\sum_{i=1}^d(n_i+1)\). Let \(\mathcal R\subset\operatorname{Gr}(d,m)\) denote the curve whose member at \(t\in\mathbb P^1\) is the row span of the block-diagonal matrix with block rows \((1,t,\ldots,t^{n_i})\), extended at infinity by \((t^{-n_i},\ldots,1)\). Use the symmetric-idempotent realization of the Grassmannian and the chordal squared-distance objective.

Set \(s_i(t)=\sum_{j=0}^{n_i}t^{2j}\), \(L(t)=\operatorname{lcm}_{1\le i\le d}s_i(t)\), and \(\delta=\deg L\). For a general complex symmetric rank-\(d\) idempotent data projector \(Q\), the distance objective on the ruling curve has exactly \(2\delta-2\) distinct complex critical points, all lying in its regular projection-matrix locus and away from the algebraic poles. Consequently
\[
\operatorname{GDdeg}(\mathcal R)=\operatorname{EDdeg}(\mathcal R)=2\delta-2
=2\sum_{e\in\mathcal E}\varphi(e)-2,
\qquad\mathcal E=\{e\in\mathbb Z:e>2,\ e\mid 2(n_i+1)\text{ for some }i\}.
\]
Here \(\varphi\) is Euler's totient function. This includes arbitrary unequal scroll multidegrees and all ranks \(d\ge2\). For example \(\operatorname{GDdeg}\mathcal R_{(2,3)}=18\) and \(\operatorname{GDdeg}\mathcal R_{(2,3,4)}=34\).

## Assumptions and scope
Work over \(\mathbb C\) with the standard nondegenerate symmetric bilinear form, its real positive-definite form as a Zariski-dense real structure, and \(d\ge2\), \(n_i\ge2\). A data projector is a complex symmetric idempotent \(Q=Q^T=Q^2\) of rank \(d\). Generic means outside a proper Zariski-closed subset of the irreducible variety of such projectors. The optimization objective is \(\operatorname{tr}(P(t)Q)\), equivalent to minimizing squared chordal distance because \(\operatorname{tr}P=\operatorname{tr}Q=d\).

The ruling curve is embedded by the parameter: either the first two coordinates of any row recover the finite parameter \(t\), or the reversed coordinates recover \(t^{-1}\) at infinity. Its projection-matrix representation is a rational map undefined precisely when at least one \(s_i(t)\) vanishes. These excluded points are not counted as Grassmann distance-critical points.

## Proof
For finite \(t\) with every \(s_i(t)\ne0\), the orthogonal projector \(P(t)\) has diagonal blocks
\[
P_i(t)=\frac{v_i(t)^T v_i(t)}{s_i(t)},\qquad v_i(t)=(1,t,\ldots,t^{n_i}).
\]
Hence the objective is \(f_Q(t)=\operatorname{tr}(P(t)Q)=\sum_i\operatorname{tr}(P_i(t)Q_{ii})\), and has denominator dividing \(L\). Each \(s_i=(t^{2(n_i+1)}-1)/(t^2-1)\) is square-free over \(\mathbb C\). At a zero \(\alpha\) of \(L\), at least one corresponding block has a nonzero simple pole with residue \(v_i(\alpha)^Tv_i(\alpha)/s'_i(\alpha)\). Distinct blocks occupy distinct coordinate spaces, so the total matrix residue \(R_\alpha=\operatorname{Res}_{t=\alpha}P(t)\) is nonzero.

**Linear-span lemma.** The complex linear span of all rank-\(d\) symmetric orthogonal projection matrices in \(\operatorname{Sym}_m(\mathbb C)\) is all of \(\operatorname{Sym}_m(\mathbb C)\) when \(1\le d<m\). Indeed, a symmetric matrix orthogonal to all rank-\(d\) projections has zero sum on every \(d\)-element diagonal subset; comparison makes all diagonal entries equal, and their sum forces these entries to vanish. Rotating a coordinate \(d\)-plane through two coordinates then forces every off-diagonal entry to vanish. Therefore \(Q\mapsto\operatorname{tr}(R_\alpha Q)\) is not identically zero. Removing finitely many proper closed sets ensures that \(f_Q\) has a genuine simple pole at each of the \(\delta\) roots of \(L\).

At infinity set \(u=t^{-1}\). The \(i\)-th block becomes the projector of \((u^{n_i},u^{n_i-1},\ldots,1)\), divided by \(1+u^2+\cdots+u^{2n_i}\). Its derivative at \(u=0\) has nonzero entries between the final and penultimate coordinates. Therefore \(P'(u)|_{u=0}\ne0\), and by the linear-span lemma, for generic \(Q\) the derivative of \(f_Q\) at infinity is nonzero. Thus the meromorphic map \(f_Q:\mathbb P^1\to\mathbb P^1\) has degree \(\delta\), with \(\delta\) simple poles and no ramification at infinity. Riemann--Hurwitz implies that its derivative has exactly \(2\delta-2\) zeros counted with multiplicity, none at poles.

It remains to verify that the critical points are generically simple even when \(Q\) is restricted to the data-projector variety \(\mathcal G=\operatorname{pGr}(d,m)\). For fixed parameter \(t\) off the poles, the incidence condition \(\operatorname{tr}(P'(t)Q)=0\) is a nonzero linear hyperplane section of \(\mathcal G\). For general real \(t\), the real symmetric matrix \(A=P'(t)\) has, in each block, one positive and one negative eigenvalue and \(n_i-1\) zero eigenvalues. It therefore has a zero eigenspace of dimension \(m-2d\ge d\) and each other eigenspace has dimension at most \(d\). A point \(Q\) is stationary for the height function \(\operatorname{tr}(AQ)\) on \(\mathcal G\) exactly when \([A,Q]=0\). If the eigenspace dimensions of \(A\) are \(m_j\), its commuting locus is a union of products \(\prod_j\operatorname{pGr}(k_j,m_j)\), \(\sum_j k_j=d\). Its dimension is at most
\[
\sum_j k_j(m_j-k_j)\le d(m-2d-1),
\]
whereas \(\dim\mathcal G=d(m-d)\). Thus the stationary locus of this height function has codimension at least \(d(d+1)>1\). The hyperplane section cannot possess a generically nonreduced irreducible component, since such a component would be contained in that stationary locus. For a generic parameter its incidence divisor is therefore reduced. No incidence component is vertical over the parameter curve (the defining linear functional is never identically zero on \(\mathcal G\)); hence the total critical incidence variety is generically reduced. Generic smoothness in characteristic zero applied to its generically finite projection to \(\mathcal G\) now gives reduced fibers over a Zariski-open set of data projectors. The \(2\delta-2\) critical points are therefore distinct, proving the formula.

Lastly, cyclotomic factorization of the \(s_i\) gives \(L=\prod_{e>2,\,e\mid2(n_i+1)\text{ for some }i}\Phi_e\), yielding the stated totient sum.

## Verification
The standalone exact-arithmetic script `check_scroll_gd.py` constructs genuine block-diagonal rank-\(d\) projection data, takes exact derivatives, and checks that the numerator of the derivative has degree \(2\delta-2\), is square-free and is coprime to its denominator. It returned `VERIFY_OK` for multidegrees \((2,3)\), \((2,4)\), \((3,5)\), \((2,2,3)\) and \((2,3,4)\). These are finite examples only; the proof above establishes the arbitrary-exponent statement.

## Relationship to prior work
Friedman--Hoşten--Rosana, arXiv:2610.02018, Theorem 2.2, prove the same totient expression for **unrestricted symmetric-matrix data**, namely the ED degree. Their full text distinguishes ED from GD and does not give the stated GD theorem for scroll ruling curves. Friedman--Rosana--Sturmfels, arXiv:2601.22843, establish the GD framework for rank-two models without the all-multidegree ruling-curve formula. The balanced multidegree case was previously available; the present new implication concerns unequal \(n_i\), the complete gcd/cyclotomic overlap pattern, and arbitrary ranks \(d\ge3\), for which generic GD finiteness is not automatic.

## Limitations
The assertion is for **general complex rank-\(d\) projector data** and the standard block-orthogonal scroll embedding; exceptional projectors can have cancellations, multiple critical points or critical points at the deleted locus. It does not calculate real critical-point counts or general GD degrees of all Grassmannian models. The novelty comparison excludes identified stronger coverage but cannot prove absolute historical priority without independent review.

## References
1. H. Friedman, S. Hoşten, A. Rosana, *Euclidean Distance Optimization Within the Grassmannian*, arXiv:2610.02018v2 (2026), Theorem 2.2 and Sections 1--4; https://arxiv.org/html/2610.02018v2.
2. H. Friedman, A. Rosana, B. Sturmfels, *Distance Optimization in the Grassmannian of Lines*, arXiv:2601.22843v1 (2026), Sections 3--4; https://arxiv.org/html/2601.22843v1.

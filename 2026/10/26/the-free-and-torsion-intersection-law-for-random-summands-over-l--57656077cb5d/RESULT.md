# The free-and-torsion intersection law for random summands over length-two chain rings

## Finding

Let \(R\) be an arbitrary **finite commutative chain ring of length exactly two**: its maximal ideal is \(\mathfrak m=(\pi)\), \(\pi^2=0\), and its residue field \(R/\mathfrak m\) has cardinality \(q\). Let \(n\ge 1\), \(0\le k,\ell\le n\), fix a rank-\(k\) free direct summand \(U\le R^n\), and choose a rank-\(\ell\) free direct summand \(V\le R^n\) uniformly from all such summands. Each intersection is a finite \(R\)-module of the unique form
\[
I=U\cap V\cong R^a\oplus (R/\mathfrak m)^b.
\]
Write \(d=a+b\) and \(c=n-k-\ell+d\). Let \({N\brack j}_q\) denote the Gaussian coefficient (zero for \(j<0\) or \(j>N\)), and set \(|\operatorname{GL}_0(\mathbb F_q)|=1\). The complete intersection-type count is
\[
\boxed{N_{n,k,\ell;q}(a,b)=
{k\brack d}_q{n-k\brack \ell-d}_q
q^{(k-d)(\ell-d)+\ell(n-\ell)-dc}
{d\brack b}_q{c\brack b}_q|\operatorname{GL}_b(\mathbb F_q)|.}
\]
It is zero unless \(0\le d\le\min(k,\ell)\), \(d\ge k+\ell-n\), and \(0\le b\le\min(d,c)\). This number is independent of the isomorphism type of the length-two chain ring with residue field \(\mathbb F_q\); in particular it applies to both dual numbers and \(\mathbb Z/4\mathbb Z\). The uniform probability is obtained by dividing by \(q^{\ell(n-\ell)}{n\brack\ell}_q\).

A second, genuinely asymptotic statement describes the critical intersection regime. Fix \(q\) and an arbitrary integer \(s\), let \(k=\ell\to\infty\), and put \(n=2k+s\). Define
\[
\Phi_j(q)=\prod_{i=1}^j(1-q^{-i}),\quad \Phi_0(q)=1,\quad \Phi_\infty(q)=\prod_{i=1}^\infty(1-q^{-i})>0.
\]
If \((A_k,B_k)\) records the free and simple cyclic multiplicities in \(U\cap V\), then \((A_k,B_k)\) converges in **total variation** to a probability law with atoms indexed by \(a,b\ge0\), \(d=a+b\ge\max(0,-s)\), and \(c=d+s\ge0\):
\[
\boxed{\Pr(A=a,B=b)=
\frac{\Phi_\infty(q)q^{-d(d+s)}}{\Phi_d(q)\Phi_{d+s}(q)}\;
\frac{{d\brack b}_q{d+s\brack b}_q|\operatorname{GL}_b(\mathbb F_q)|}{q^{d(d+s)}}.}
\]
Equivalently, sample the residue intersection dimension \(D\) from
\[
\Pr(D=d)=\frac{\Phi_\infty(q)q^{-d(d+s)}}{\Phi_d(q)\Phi_{d+s}(q)},
\]
then, conditionally on \(D=d\), let \(B\) have the rank law of a uniform \((d+s)\)-by-\(d\) matrix over \(\mathbb F_q\) and put \(A=d-B\). These formulas give a ring-independent limit and distinguish torsion intersections from intersections that contain free direct summands.

In the balanced case \(s=0\), the limits for trivial intersection and for having no free cyclic summand are, respectively,
\[
\Pr(U\cap V=0)\longrightarrow\Phi_\infty(q),\qquad
\Pr(A_k=0)\longrightarrow
\Phi_\infty(q)\sum_{d=0}^{\infty}\frac{q^{-d^2}}{\Phi_d(q)}.
\]
For \(q=2\) these are approximately \(0.2887880951\) and \(0.6274408698\). Thus the limiting probability of a **nonzero torsion-only intersection** is approximately \(0.3386527747\), a phenomenon that does not exist for intersections of vector subspaces over fields.

## Assumptions and scope

All rings are finite, commutative, principal, local and have radical nilpotency length two. The residue-field order \(q\) is any prime power. The finite formula permits unequal free ranks, arbitrary nonnegative free and torsion multiplicities, and all valid dimensions including \(k=0\) or \(\ell=0\). The asymptotic formula keeps \(q\) and \(s\) fixed while \(k\to\infty\). The choice of the fixed summand \(U\) does not matter by transitivity of \(\operatorname{GL}_n(R)\). The statement is **not** a claim about nonfree input summands, rings of length three or greater, or noncommutative chain rings.

## Proof

**1. Lift count.** Write \(F=R/\mathfrak m\) and let \(H\subset F^n\) be the image of \(U\) modulo \(\mathfrak m\). A free rank-\(\ell\) direct summand reduces to an \(\ell\)-plane \(L\subset F^n\). For fixed \(L\), choose a complementary \(R\)-direct summand \(W\) to one lift \(V_0\). Every other lift of the same \(L\) is uniquely the graph of an \(R\)-linear map \(V_0\to\mathfrak m W\), and these maps form an \(F\)-vector space of dimension \(\ell(n-\ell)\). Hence there are exactly \(q^{\ell(n-\ell)}\) lifts, proving the denominator asserted above.

**2. Residue intersection count.** Set \(S=L\cap H\) with \(\dim_F S=d\). Choose \(S\) in \(H\), and the image of \(L\) in \(F^n/H\). Their dimensions are \(d\) and \(\ell-d\). Each choice admits \(q^{(k-d)(\ell-d)}\) graph maps, so the number of residue planes \(L\) with this \(d\) is
\[
{k\brack d}_q{n-k\brack \ell-d}_q q^{(k-d)(\ell-d)}.
\]
We have \(\dim_F(F^n/(L+H))=c=n-k-\ell+d\).

**3. Canonical obstruction map.** For \(x\in S\), select a lift of \(x\) in \(V\) and one in \(U\). Their difference belongs to \(\mathfrak m R^n\). The class of this difference modulo \(\mathfrak m(U+V)\) depends only on \(x\), up to the natural canonical identification with \(F^n/(L+H)\). The resulting connecting morphism
\[
\delta_V:S\longrightarrow F^n/(L+H)
\]
is \(F\)-linear. Its kernel is exactly the image of \(I=U\cap V\) in \(F^n\). Under the graph parametrization in step 1, \(\delta_V\) changes by restriction followed by quotient, namely the surjective linear map
\[
\operatorname{Hom}_F(L,F^n/L)\longrightarrow
\operatorname{Hom}_F(S,F^n/(L+H)).
\]
Its target has dimension \(dc\). Thus \(\delta_V\) is uniform on all \(c\)-by-\(d\) matrices when \(V\) is uniform among lifts of \(L\). Each such obstruction map is realized by exactly \(q^{\ell(n-\ell)-dc}\) lifts.

**4. Smith type.** The radical-annihilated subgroup satisfies
\[
I[\mathfrak m]=\mathfrak m U\cap\mathfrak m V\cong F^d,
\]
so an intersection of type \(R^a\oplus F^b\) has \(a+b=d\). Its reduction image in \(F^n\) has dimension \(a=\dim_F\ker\delta_V\). Therefore \(b=\operatorname{rank}_F\delta_V\). A standard image-and-kernel count gives exactly
\[
\#\{T:F^d\to F^c:\operatorname{rank}T=b\}
={d\brack b}_q{c\brack b}_q|\operatorname{GL}_b(F)|.
\]
Multiplying the independent counts from steps 1–4 proves the complete finite formula. Summing over all \((a,b)\) uses the rank partition of \(\operatorname{Hom}_F(F^d,F^c)\), confirming the number \(q^{\ell(n-\ell)}{n\brack\ell}_q\) of possible summands.

**5. Critical-window limit.** In the equal-rank regime \(n=2k+s\), step 2 yields the exact residue dimension law
\[
\Pr(D_k=d)=
\frac{{k\brack d}_q{k+s\brack k-d}_q q^{(k-d)^2}}{{2k+s\brack k}_q},
\qquad d\ge\max(0,-s).
\]
The Gaussian identity \({m\brack j}_q=q^{j(m-j)}\Phi_m(q)/(\Phi_j(q)\Phi_{m-j}(q))\) shows pointwise convergence to the stated \(D\)-mass. Since every \(\Phi_m(q)\) lies in \([\Phi_\infty(q),1]\), the exact masses are uniformly bounded, for fixed \(q,s\), by a constant multiple of \(q^{-d(d+s)}\). This is a summable majorant. Dominated convergence therefore proves total-variation convergence of \(D_k\). By step 3, conditionally on \(D_k=d\), the torsion multiplicity has the rank distribution of a uniform \((d+s)\)-by-\(d\) field matrix; its law does not depend on \(k\). Passing through this common stochastic kernel preserves total-variation convergence and proves the joint limit. For \(s=0\), conditional full rank occurs with probability \(\Phi_d(q)\); substituting into the joint law yields the balanced specializations.

## Verification

The companion self-contained file `verify_intersections.py` independently constructs every free summand of small finite length-two rings by reduced-row-echelon residue planes and exhaustive lift parameters. It constructs actual intersections by enumeration of all ring-linear combinations and classifies each intersection through its cardinality and reduction image. Ten configurations over \(\mathbb F_2[\varepsilon]/(\varepsilon^2)\) and \(\mathbb F_3[\varepsilon]/(\varepsilon^2)\) and six configurations over \(\mathbb Z/4\mathbb Z\) match **every** predicted free/torsion coefficient. Separately, finite Gaussian normalization identities are tested for \(q=2,3,4,5,7\), \(1\le n\le9\), and all valid ranks. The tests verify finite instances but are not an infinite proof; the general conclusions are established by the five proof steps.

## Relationship to prior work

Byrne, Horlemann, Khathuria and Weger give general finite-chain-ring submodule-type counts and density limits for the proportion of all submodules that are free. Their analysis supplies context, not the distribution for intersections of **two randomly selected free summands**. Cao's earlier classification of general-linear-group orbitals on right-invertible matrices is a genuinely close and potentially stronger finite-parameter framework: summing framed-matrix orbits could recover substantial finite enumerative information here. We do **not** claim that framed-orbit theory or ordinary Grassmann intersection numbers are new. The distinct result emphasized here is the exact free-versus-torsion intersection law with its residue-matrix disintegration and fixed-field critical-window **joint probability limit**, including rings of mixed characteristic. Landjev, Rogachev and Rousseva study extremal intersecting families of free chain-ring submodules; their Hjelmslev setting acknowledges that intersections can be nonfree, but their extremal theorem does not give this random joint law. These are statements about inspected material, not an exhaustive priority claim.

## Limitations

The finite formula may be derivable by orbit-summing from Cao's 2011 general orbital theory; publication priority for that component is not claimed. The proof does not address input submodules that are nonfree or chain length larger than two. The probability law concerns uniformly selected direct summands, not uniformly selected arbitrary submodules. The critical limit assumes fixed field order and fixed codimension offset; no uniformity in growing \(q\) or \(s\) is established. No independent audit has been performed.

## References

1. E. Byrne, A.-L. Horlemann, K. Khathuria, V. Weger, *Density of Free Modules over Finite Chain Rings*, arXiv:2106.09403 (initial public version 2021-06-17); *Linear Algebra and its Applications* **651** (2022), 1–25. DOI: 10.1016/j.laa.2022.06.013. Full open-access source: https://arxiv.org/html/2106.09403v2.
2. Y. Cao, *Association Schemes and Directed Graphs Determined by Orbitals of General Linear Groups Over Finite Chain Rings*, *Communications in Algebra* **39** (2011), 220–236. DOI: 10.1080/00927870903390652. Primary text inspected in an accessible full-text rendering; Theorems 3.2–3.3.
3. I. Landjev, E. Rogachev, A. Rousseva, *A Chain Ring Analogue of the Erdős-Ko-Rado Theorem*, arXiv:2602.12219 (initial public version 2026-02-12), especially discussion of nonfree intersections and the extremal-family statements. Full source: https://arxiv.org/abs/2602.12219.

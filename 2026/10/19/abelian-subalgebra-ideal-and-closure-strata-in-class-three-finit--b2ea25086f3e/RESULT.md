# Abelian subalgebra, ideal and closure strata in class-three finite Lie algebras of two breadths

## Finding

Let \(q\) be an odd prime power, \(m\geq1\), \(k=\mathbb F_q\), and \(K=\mathbb F_{q^m}\). Put \(Q=q^m\) and \(\Lambda=Q^2+Q+1\). Consider the \(5m\)-dimensional \(k\)-Lie algebra \(L=K^5\) with bracket, for \(v=(a,b,c,d,e)\) and \(w=(x,y,z,u,v')\),
\[
[v,w]=(0,0,t,t+2cx-2az,t+2bz-2cy),\qquad t=ay-bx.
\]
This algebra is the explicit family classified by Kundu, Naik and Singh [KNS]. Their classification identifies it, up to isomorphism, with every finite-dimensional, class-three, **stem** Lie algebra over \(k\) of breadth type \((0,2m)\). We do not reprove or claim that classification.

Let \(Z=Z(L)=\{(0,0,0,d,e):d,e\in K\}\), and write \(\pi:L\longrightarrow K^3\) for the projection onto the first three coordinates. For a \(k\)-subspace \(H\leq L\), define \(r=\dim_k\pi(H)\) and \(s=\dim_k(H\cap Z)\). Write \({n\brack j}_q\) for the Gaussian coefficient, with \({n\brack j}_q=0\) outside \(0\leq j\leq n\).

**Complete abelian-subalgebra census.** Every abelian \(k\)-Lie subalgebra \(H\) satisfies \(0\leq s\leq 2m\) and either \(r=0\) or \(1\leq r\leq m\). The number in each stratum is exactly
\[
N_{r,s}=\begin{cases}
{2m\brack s}_q,&r=0,\\[3pt]
\Lambda\,{m\brack r}_q{2m\brack s}_q\,q^{r(2m-s)},&1\leq r\leq m.
\end{cases}
\]
In particular, the abelian-subalgebra dimension polynomial is
\[
A_{m,q}(T)=\sum_{s=0}^{2m}{2m\brack s}_qT^s
\left(1+\Lambda\sum_{r=1}^{m}{m\brack r}_q q^{r(2m-s)}T^r\right).
\]
The coefficient of \(T^j\) is the exact number of abelian \(j\)-dimensional \(k\)-subalgebras, for every \(0\leq j\leq5m\).

**Projective spread, ideals and closure.** The inclusion-maximal abelian subalgebras are exactly \(A_\ell=\pi^{-1}(\ell)\), where \(\ell\) ranges over the \(\Lambda\) one-dimensional \(K\)-subspaces of \(K^3\). Each has dimension \(3m\), two distinct ones intersect in \(Z\), and every noncentral abelian subalgebra lies in a unique \(A_\ell\). Put \(\ell_0=K(0,0,1)\) and \(B=A_{\ell_0}=L'\). The normalizer of \(B\) is all of \(L\), whereas every other \(A_\ell\) has normalizer dimension \(4m\) over \(k\).

The complete abelian-**ideal** dimension polynomial is
\[
I_{m,q}(T)=\sum_{s=0}^{2m}{2m\brack s}_q T^s+T^{2m}\sum_{r=1}^{m}{m\brack r}_qT^r.
\]
Indeed the abelian ideals are precisely all subspaces of \(Z\), together with all \(Z\oplus P\), where \(P\) is any nonzero \(k\)-subspace of \(K(0,0,1,0,0)\). In particular, \(B\) is the unique maximal abelian ideal.

More precisely, for an abelian \(H\), write \(\langle H\rangle_{\mathrm{ideal}}\) for its generated Lie ideal. If \(r=0\), this ideal is \(H\) itself. If \(r\geq1\), the projective \(K\)-line \(\ell\) containing \(\pi(H)\) is uniquely determined, and
\[
\dim_k\langle H\rangle_{\mathrm{ideal}}=
\begin{cases}
2m+r,&\ell=\ell_0,\\
3m+r,&\ell\neq\ell_0.
\end{cases}
\]
For fixed \((r,s)\) with \(r\geq1\), exactly \({m\brack r}_q{2m\brack s}_q q^{r(2m-s)}\) abelian subalgebras have the first closure dimension, and exactly \((\Lambda-1){m\brack r}_q{2m\brack s}_q q^{r(2m-s)}\) have the second. These are not claims about all Lie subalgebras, only abelian ones.

## Assumptions and scope

The base field \(k\) may be any finite field of **odd** characteristic; the extension degree \(m\) may be arbitrary and need not be coprime to the characteristic. Every subalgebra and ideal here is \(k\)-linear; it need not be \(K\)-linear. An abelian subalgebra means a vector subspace on which the displayed bracket vanishes identically. A Lie ideal means an additive \(k\)-subspace stable under bracketing with all of \(L\). "Maximal" means maximal under inclusion, not merely an isolated local dimension optimum. The full family has breadth types \((0,2m)\) and nilpotency class three by [KNS]; identifying all such stem algebras with this family uses their theorem, not a new classification. Characteristic two is excluded because the rank-three wedge criterion used below requires \(2\) to be invertible.

## Proof

**Step 1 — exact commuting condition.** Direct expansion of the bracket shows that \([v,w]=0\) if and only if
\[
ay-bx=0,\qquad cx-az=0,\qquad bz-cy=0.\]
The factor \(2\) is invertible in \(k\). These are the three two-by-two minors of the matrix with rows \((a,b,c)\) and \((x,y,z)\), up to signs. Thus \([v,w]=0\) holds if and only if \(\pi(v)\) and \(\pi(w)\) are dependent **over \(K\)**. If a \(k\)-subspace \(H\) is abelian and \(\pi(H)\neq0\), choosing one nonzero \(\pi(v)\) forces every vector of \(\pi(H)\) to lie in the same unique one-dimensional \(K\)-space \(\ell=K\pi(v)\). Conversely, every \(k\)-subspace with projection contained in such a line is abelian. This is a complete characterization, including the case \(\pi(H)=0\).

**Step 2 — enumeration.** The center \(Z\) has \(k\)-dimension \(2m\). When \(r=0\), every \(H\) is an \(s\)-subspace of \(Z\), giving \({2m\brack s}_q\). When \(r\geq1\), choose a unique projective line \(\ell\) in \(K^3\) in \(\Lambda=(Q^3-1)/(Q-1)\) ways, an \(r\)-dimensional \(k\)-subspace \(P\leq\ell\) in \({m\brack r}_q\) ways, and an \(s\)-dimensional \(k\)-subspace \(S\leq Z\) in \({2m\brack s}_q\) ways. With \(L=K^3\oplus Z\), every \(H\) with \(\pi(H)=P\) and \(H\cap Z=S\) is uniquely the inverse image of the graph of a \(k\)-linear map \(P\to Z/S\) in \(P\oplus(Z/S)\). There are \(q^{r(2m-s)}\) maps. No two choices of \(\ell\) duplicate a noncentral \(H\). This proves the full formula and generating polynomial. It also shows that every noncentral \(H\) extends uniquely to the abelian algebra \(\pi^{-1}(\ell)\), while a central \(H\) extends into every such algebra. The maximal objects are therefore exactly the \(A_\ell\), all of dimension \(3m\), and distinct \(A_\ell\) intersect in \(Z\).

**Step 3 — normalizer and ideal dichotomy.** Let \(\ell=K(a,b,c)\). The commutator of any element of \(L\) with \(A_\ell\) lies in \(L'=K(0,0,1,0,0)\oplus Z\). If \((a,b)\neq(0,0)\), then \(A_\ell\cap L'=Z\), so \(x\in N_L(A_\ell)\) if and only if the third coordinate of \([x,(a,b,c,0,0)]\) is zero. This is one nonzero \(K\)-linear equation in the first two coordinates of \(\pi(x)\), with the third and both central coordinates free. Hence \(\dim_kN_L(A_\ell)=4m\). If \((a,b)=(0,0)\), the line is \(\ell_0\) and \(A_{\ell_0}=L'\), an ideal, so its normalizer is \(L\).

For any noncentral abelian ideal \(J\), choose \(0\neq\pi(v)\in\pi(J)\), lying in the unique line \(\ell\). If \((a,b)\neq(0,0)\), a suitable \(x\in L\) has third coordinate of \([x,v]\) nonzero, while \([x,v]\in J\subseteq A_\ell\) would force that coordinate to vanish because \(A_\ell\cap L'=Z\); contradiction. Therefore every noncentral abelian ideal lies in \(B=L'\). For a nonzero \(c\in K\), the brackets of \((0,0,c,d,e)\) with elements of \(L\) span all \(Z\): indeed the fourth and fifth coordinates independently run through all of \(K\). Thus a noncentral abelian ideal must contain \(Z\) and is exactly \(Z\oplus P\) for some nonzero \(k\)-subspace \(P\leq K(0,0,1,0,0)\). Conversely each such \(Z\oplus P\) is clearly an abelian ideal, as are all subspaces of \(Z\). Counting them proves \(I_{m,q}(T)\).

**Step 4 — generated ideals.** For a noncentral abelian \(H\subseteq A_{\ell_0}\), brackets of one element with nonzero third coordinate already span \(Z\), whence \(\langle H\rangle_{\mathrm{ideal}}=H+Z\), of dimension \(2m+r\). If instead \(\ell\neq\ell_0\), some \(v\in H\) has \((a,b)\neq(0,0)\). The map \(x\mapsto ay-bx\) is surjective onto \(K\); therefore \([L,v]\) maps onto \(K(0,0,1,0,0)\) modulo \(Z\). Iterated brackets \([L,[L,v]]\) span \(Z\), since some bracket in \([L,v]\) has a nonzero third coordinate. The ideal generated by \(H\) consequently contains \(L'\), and \(H+L'\) is itself an ideal (because \([L,H]\subseteq L'\) and \(L'\) is an ideal). Thus \(\langle H\rangle_{\mathrm{ideal}}=H+L'\). As \(H\cap L'=H\cap Z\), its dimension is \((r+s)+3m-s=3m+r\). Splitting the \(\Lambda\) projective lines into one exceptional line and \(\Lambda-1\) others in Step 2 gives the asserted closure-fiber counts.

All steps are algebraic identities and finite-dimensional subspace enumerations, so no extrapolation from finite experiments is used.

## Verification

The companion `verify_abelian_breadth.py` enumerates **every** linear subspace of \(\mathbb F_q^5\), tests pairwise brackets directly, tests ideal stability against a basis, and calculates ideal closures by iterated brackets. It independently compares all resulting counts with the formulas for \(q=3\) and \(q=5\): there are \(2664\) and \(42176\) ambient subspaces respectively, of which \(292\) and \(1744\) are abelian. Their dimension distributions are \((1,121,157,13)\) and \((1,781,931,31)\); their abelian-ideal distributions are \((1,4,1,1)\) and \((1,6,1,1)\). The corresponding ideal-closure dimension distributions are \((1,4,1,22,264)\) and \((1,6,1,56,1680)\). The script also realizes \(\mathbb F_9=\mathbb F_3[T]/(T^2+1)\), enumerates its \(91\) projective lines, checks pairwise commutativity in each, verifies one full-normalizer line and \(90\) codimension-one normalizer lines, and tests \(12000\) seeded vector pairs. Formula values for \((q,m)=(3,2)\) give \((1,29524,990301,3079480,1001911,33124,91)\). These finite checks are not a proof for arbitrary fields and extension degrees; Steps 1–4 supply that proof.

Run with a standard Python interpreter from the folder containing the file: `python verify_abelian_breadth.py`. It needs no external packages.

## Relationship to prior work

[KNS] explicitly defines \(L\), determines its derived series and breadth, and classifies the ambient stem algebras. In particular their Proposition 3.2 supplies centralizer equations closely related to Step 1. Their published structural theorem is not newly claimed. Our claim is the finer **enumeration of all \(k\)-linear abelian subalgebras and abelian ideals**, simultaneous ideal-closure fibers, and normalizer distribution in every extension degree. This includes \(k\)-subspaces that are not \(K\)-linear, which prevents replacing \({m\brack r}_q\) by a trivial count of \(K\)-subspaces. The earlier paper's centralizer data substantially motivates and simplifies the derivation; originality is limited to the resulting quantitative stratification and exact ideal-closure classification, not to field-spread geometry itself.

[BD] treats indices and maximal abelian dimensions of free nilpotent Lie algebras in characteristic zero. Its Example 3.3 already identifies the maximum abelian dimension as three in the five-dimensional two-generator class-three case. That maximum-dimension fact is excluded from any originality claim here. [BC] surveys the structural theory of free nilpotent Lie algebras in characteristic zero; its focus is derivations, automorphisms and associated structures, not finite-field subalgebra-number stratifications. Searches also compared published findings on the Heisenberg subalgebra-commutativity degree and on adjoint-rank spectra of filiform Lie algebras. The former concern a different class-two Lie algebra and a probability over pairs of subalgebras; the latter concern centralizer ranks rather than the exact incidence-and-ideal counts here.

## Limitations

Only odd characteristic is covered. The enumeration is for **abelian** subalgebras and abelian ideals, not all subalgebras or all ideals. It is a count of labelled embedded subspaces, not a classification modulo automorphisms. The classification of the underlying breadth-type Lie algebras is taken from [KNS]. Unsearched or unindexed older finite-field Lie-algebra enumerations could contain an equivalent formula; the absence of a discovered match is not proof of historical priority. Independent mathematical audit has not been performed.

## References

[KNS] R. Kundu, T. K. Naik, A. Singh, *Nilpotent Lie algebras with two centralizer dimensions over a finite field*, arXiv:2208.07676 (first publicly posted 2022-08-16), Theorem 1.3, Corollary 1.4, Proposition 3.2, and Sections 4–5. https://arxiv.org/abs/2208.07676

[BD] D. Burde, K. Dekimpe, *The index of nilpotent Lie algebras*, arXiv:2505.08331 (2025), Example 3.3 and Section 3. https://arxiv.org/abs/2505.08331

[BC] P. Benito, D. de-la-Concepción, *An overview of free nilpotent Lie algebras*, Commentationes Mathematicae Universitatis Carolinae 55 (2014), 325–339. https://investigacion.unirioja.es/documentos/5bbc696ab750603269e81ac8/f/617a4e5f2bb80f973acc38e7.pdf

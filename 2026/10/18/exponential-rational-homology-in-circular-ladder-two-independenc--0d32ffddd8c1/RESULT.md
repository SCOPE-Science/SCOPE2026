# Exponential rational homology in circular-ladder two-independence complexes

## Finding
For every integer \(n\ge3\), consider the circular ladder \(L_n=C_n\square K_2\) and its two-independence complex \(X_n=\operatorname{Ind}_2(L_n)\). Let
\[
P_n(z)=\sum_{\sigma\in X_n}z^{|\sigma|},\qquad E_n=P_n(-1)=-\widetilde\chi(X_n).
\]
There is an explicit sixteen-state transfer matrix determining the **entire face polynomial** \(P_n(z)\) for every \(n\ge3\), and its characteristic polynomial is
\[
\det(tI-T(z))=t^{10}(t^2+zt+z^2)
\bigl[t^4-(z+1)t^3-(2z^2+z)t^2+(z^3-z^2)t+z^4\bigr].
\]
In particular the signed face sums satisfy, for every \(n\ge3\),
\[
E_{n+6}=E_{n+5}+E_{n+3}-2E_{n+2}+3E_{n+1}-E_n,
\]
with \((E_3,E_4,E_5,E_6,E_7,E_8)=(4,-3,11,10,1,29)\). The values are **never zero**: \(E_4=-3\), and \(E_n>0\) whenever \(n\ge3\) and \(n\ne4\).

Let \(\alpha\in(1.386,1.387)\) be the larger positive root of \(q(t)=t^4-t^2-2t+1\). Then
\[
E_n=\alpha^n+O(1.31^n),\qquad
\sum_{j\ge0}\dim_{\mathbb Q}\widetilde H_j(X_n;\mathbb Q)
\ge |E_n|>\frac{(1.386)^n}{3}\quad(n\ge20).
\]
Thus **every** such higher-independence complex is noncontractible and carries exponentially growing total rational homology. The full homotopy type is not determined.

## Assumptions and scope
The graph \(C_n\), for \(n\ge3\), is the simple cycle on the cyclic index set \(\mathbb Z/n\mathbb Z\). Vertices of \(L_n\) are \((i,r)\), for \(i\in\mathbb Z/n\mathbb Z\) and \(r\in\{0,1\}\); edges join consecutive indices in the same layer and the two layers at the same index. The complex \(X_n\) consists precisely of subsets whose induced subgraphs have maximum degree at most one: every connected component of a simple graph has at most two vertices if and only if every vertex has induced degree at most one. The empty subset is included. Ordinary geometric realization and reduced rational simplicial homology are used.

## Proof
**1. Local constraint and exact transfer.** Encode column \(i\) by \(b_i\in\{0,1,2,3\}\), whose binary digits record chosen vertices in the two layers. For digits \(a,b,c\in\{0,1,2,3\}\), define the predicate \(J(a,b,c)\) by requiring, for both \(r\in\{0,1\}\) with the \(r\)-th bit of \(b\) equal to one,
\[
[a_r=1]+[c_r=1]+[b_{1-r}=1]\le1.
\]
Here brackets are zero-one truth values. It is exactly the induced degree constraint at each selected vertex of the middle column. Index rows and columns of \(T(z)\) by ordered pairs \((a,b)\), and set
\[
T(z)_{(a,b),(b',c)}=
\begin{cases}
 z^{\operatorname{popcount}(c)},&b=b'\text{ and }J(a,b,c),\\
 0,&\text{otherwise.}
\end{cases}
\]
For \(n\ge3\), a cyclic sequence \((b_0,\ldots,b_{n-1})\) is a face if and only if its every consecutive triple satisfies \(J\). It determines exactly one based length-\(n\) closed walk through states \((b_{i-1},b_i)\). Along that walk, every selected vertex contributes its fugacity exactly once. Therefore
\[
P_n(z)=\operatorname{tr}(T(z)^n)\qquad(n\ge3).
\]
There is no division by the cyclic order: indices of the ladder are fixed and each based walk records its indexed column sequence.

**2. Exact characteristic polynomial.** Expanding the explicitly defined sixteen-by-sixteen determinant over \(\mathbb Z[z,t]\) gives
\[
\det(tI-T(z))=
 t^{10}(t^2+zt+z^2)
 (t^4-(z+1)t^3-(2z^2+z)t^2+(z^3-z^2)t+z^4).
\]
Equivalently, the nonnilpotent factor of \(\det(I-uT(z))\) is
\[
(1+zu+z^2u^2)
(1-(z+1)u-(2z^2+z)u^2+(z^3-z^2)u^3+z^4u^4).
\]
The attached exact symbolic program independently expands this determinant and compares its coefficients over the integers; the transfer construction makes this a proof for all \(n\), not an extrapolation from small cases.

**3. Signed recurrence.** At \(z=-1\), the nonzero eigenvalues, counted with algebraic multiplicity, are the roots of
\[
(t^2-t+1)\,(t^4-t^2-2t+1)
=t^6-t^5-t^3+2t^2-3t+1.
\]
Because traces of positive powers equal power sums of eigenvalues even for nontrivial Jordan blocks, the displayed order-six recurrence follows for every \(n\ge3\). Direct expansion gives the six initial values in the finding.

**4. Every signed sum is nonzero.** Write \(q(t)=t^4-t^2-2t+1\). Its derivative satisfies
\[
q'(t)=2(t-1)(2t^2+2t+1).
\]
The quadratic factor is strictly positive on the real line, so \(q\) decreases until one and increases afterward. Exact rational evaluations show that its two real roots satisfy \(0.425<\delta<0.430\) and \(1.386<\alpha<1.387\). Both are positive; its other roots are a conjugate pair of modulus \(\rho=(\delta\alpha)^{-1/2}<1.31\). The two roots of \(t^2-t+1\) have unit modulus. Therefore
\[
E_n\ge\alpha^n-\delta^n-2\rho^n-2
>\alpha^n\bigl[1-(0.430/1.386)^n-2(1.31/1.386)^n-2/(1.386)^n\bigr].
\]
Exact rational arithmetic establishes
\[
(0.430/1.386)^{20}+2(1.31/1.386)^{20}+2/(1.386)^{20}<\tfrac23.
\]
Every ratio in this expression is strictly smaller than one, so for all \(n\ge20\) one has \(E_n>\alpha^n/3>(1.386)^n/3>0\). The remaining values for \(3\le n\le19\), computed by the exact recurrence, are
\[
4,-3,11,10,1,29,4,21,67,6,105,113,44,317,171,298,761.
\]
All but the second are positive. The spectral expression also yields \(E_n=\alpha^n+O(1.31^n)\).

**5. Topological consequence.** For any nonempty finite simplicial complex with the empty face counted in its face polynomial, \(P(-1)=-\widetilde\chi\). Euler–Poincaré over \(\mathbb Q\) gives
\[
\left|\widetilde\chi(X_n)\right|\le
\sum_{j\ge0}\dim_{\mathbb Q}\widetilde H_j(X_n;\mathbb Q).
\]
Since \(E_n=-\widetilde\chi(X_n)\ne0\), each complex has nonzero reduced rational homology and cannot be contractible. The exponential lower bound follows from step 4.

## Verification
Run `python verify_prism.py` with the version of SymPy specified in `requirements.txt`. The exact symbolic check reconstructs the transfer matrix and verifies the full characteristic polynomial. A separate exhaustive bitmask program, using actual graph adjacencies rather than triple-state constraints, matches **every coefficient** of \(P_n(z)\) for \(3\le n\le8\). Exact integer traces reproduce signed terms through index nineteen; rational root evaluations and the spectral error bound are checked without floating-point assumptions. The symbolic determinant and all-parameter transfer bijection, not the finite enumeration, establish the theorem for unbounded \(n\).

## Relationship to prior work
Deshpande and Singh introduced a systematic topological treatment of higher independence complexes and computed homotopy types for complete multipartite graphs, fully whiskered graphs, paths, cycles, and perfect rooted trees [1]. These do not include cubic circular ladders. Abdelmalek and collaborators study higher-independence shellability for chordal families [2]; \(C_n\square K_2\) contains an induced four-cycle and is not chordal. Tu, Xiao, and Lang analyze the dissociation polynomial of cubic graphs but their main inequality assumes **positive** fugacity [3], which does not determine its signed value at \(-1\) or the topological consequences here. Ordinary independence, matching, total-cut, Čech, and Rips complexes of the same ladder graph are distinct constructions. No inspected statement supplies this exact order-six signed recurrence or proves noncontractibility and exponential rational homology for every circular ladder.

## Limitations
This theorem specifies the signed face polynomial, full face-enumerator transfer, and **a lower bound on total rational Betti number**. It does not compute the separate Betti numbers, integral torsion, attaching maps, or full homotopy type. The originality comparison is limited to inspected primary literature, accessible indexed mathematical results, and named search variants; undiscovered equivalent work remains possible. No independent mathematical audit has been carried out.

## References
[1] P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448, first publicly posted 2020-01-15. https://arxiv.org/abs/2001.05448

[2] F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy, and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863, first publicly posted 2021-06-21. https://arxiv.org/abs/2106.10863

[3] J. Tu, J. Xiao, and R. Lang, *Counting the number of dissociation sets in cubic graphs*, AIMS Mathematics 8 (2023), 10021–10032, first publicly posted 2023-02-23, DOI:10.3934/math.2023507. https://doi.org/10.3934/math.2023507

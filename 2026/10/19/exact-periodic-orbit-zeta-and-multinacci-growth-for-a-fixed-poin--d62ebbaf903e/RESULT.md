# Exact periodic-orbit zeta and multinacci growth for a fixed-point-free interval map

## Finding

For every integer \(k\ge2\), consider the discontinuous four-branch map \(T_k:[-k,k)\to[-k,k)\),
\[
T_k(x)=\begin{cases}
x+1,&-k\le x\le-1,\\
k(x+1),&-1<x<0,\\
k(x-1),&0\le x<1,\\
x-1,&1\le x<k.
\end{cases}
\]
The definitions agree at \(x=-1\) and \(x=1\). This family is the integer-central-gain, unit-outer-slope specialization of the García-Grimaldo–Campos-Cantón four-branch map after amplitude rescaling. It has no fixed points. For every \(n\ge1\), let \(P_n(k)=\#\{x\in[-k,k):T_k^n(x)=x\}\). Define \(S_k(t)=t+t^2+\cdots+t^k\). Then
\[
\boxed{\zeta_{T_k}(t)=\exp\!\left(\sum_{n\ge1}\frac{P_n(k)}n t^n\right)
=\frac{1-t^{k+1}}{1-S_k(t)^2}.}
\]
This identity is exact as a formal power series, not an asymptotic approximation. It includes the unique physical boundary cycle \(0\mapsto-k\mapsto-k+1\mapsto\cdots\mapsto-1\mapsto0\), of least period \(k+1\).

Let \(A_k\) be the \(2k\)-state transition matrix defined below. Equivalently, for all \(n\ge1\),
\[
\boxed{P_n(k)=\operatorname{tr}(A_k^n)-(k+1)\mathbf1_{\{k+1\mid n\}}.}
\]
Writing \(\beta_k>1\) for the unique positive solution of \(\sum_{j=1}^k\beta_k^{-j}=1\), the exponential periodic-point growth rate is
\[
\boxed{\lim_{n\to\infty}\frac1n\log P_n(k)=\log\beta_k.}
\]
The entropy of the associated finite-state symbolic itinerary system is also \(\log\beta_k\). In particular \(\beta_2=(1+\sqrt5)/2\) and \(\beta_k\uparrow2\). The entropy terminology here refers to the explicitly defined symbolic coding; no ambiguity about a topological entropy convention for a discontinuous map is needed.

## Assumptions and scope

The parameter \(k\) is an arbitrary integer at least two. The ambient real domain is the half-open forward-invariant interval \([-k,k)\), with the stated one-sided convention at the discontinuity \(x=0\); all initial points, including integer partition endpoints, are included. Multiplying every coordinate by a positive constant simply restores the original amplitude parameter without changing periodic-point counts. For finite \(n\), \(P_n(k)\) counts individual solutions of \(T_k^n(x)=x\), not primitive cycles. The zeta counts all least periods through the usual divisor/Möbius relations. There is no claim about finite-precision FPGA implementations or any different parameter regime.

## Proof

**1. Exact Markov partition.** Divide \([-k,k)\) into the \(2k\) unit half-open intervals
\[
N_j=[-j,-j+1),\qquad P_j=[j-1,j),\qquad 1\le j\le k.
\]
For the negative inner cell \(N_1\), the image is all positive cells; for the positive inner cell \(P_1\), the image is all negative cells. Every outer cell moves one unit toward the inner cell. Thus the complete transition graph is
\[
N_1\longrightarrow\{P_1,\ldots,P_k\},\quad
P_1\longrightarrow\{N_1,\ldots,N_k\},\quad
N_j\longrightarrow N_{j-1},\quad
P_j\longrightarrow P_{j-1}\quad(j\ge2).
\]
All inclusions hold with the specified half-open endpoint convention. Let \(A_k\) be its zero-one adjacency matrix, whose rows and columns are ordered \(N_k,\ldots,N_1,P_1,\ldots,P_k\).

**2. Symbolic periodic paths and their fixed representatives.** Every graph cycle necessarily visits both inner cells and therefore its affine composite has slope \(k^r\) for some \(r\ge2\). The inverse branches, extended to closed interval endpoints, map target-cell closures into source-cell closures. Consequently a closed symbolic cycle has a unique fixed representative in the closure of its starting cell: its inverse return map is a strict contraction. If that representative avoids cell endpoints, it belongs to the actual half-open cells, provides one genuine orbit point, and is uniquely coded. All cell endpoints are integers. Each integer endpoint eventually reaches \(0\); among them, exactly the \(k+1\) points \(0,-k,-k+1,\ldots,-1\) form a periodic orbit. The map is increasing on every branch and continuous at all cell endpoints except \(0\). Hence this exceptional orbit has two periodic one-sided symbolic codings: the physical right germ \(0^+\to(-k)^+\to\cdots\to(-1)^+\to0^+\), and the nonphysical left germ \(0^-\to k^-\to\cdots\to1^-\to0^-\). Every other endpoint germ is preperiodic to one of these. Thus the graph has exactly **one surplus primitive symbolic orbit**, of length \(k+1\); no other symbolic periodic orbit is lost or duplicated. In particular, for each \(n\), the number of physical fixed points is \(\operatorname{tr}(A_k^n)-(k+1)\mathbf1_{\{k+1\mid n\}}\).

**3. Determinant and zeta.** Between the two inner-cell hubs, each excursion has length \(j\) for exactly one \(j\in\{1,\ldots,k\}\). Eliminating the deterministic outer-cell strings in \(I-tA_k\) leaves the two-hub matrix with off-diagonal entry \(-S_k(t)\), and therefore
\[
\det(I-tA_k)=1-S_k(t)^2.
\]
The elementary identity \(\exp(\sum_{n\ge1}\operatorname{tr}(A_k^n)t^n/n)=\det(I-tA_k)^{-1}\) is an identity of formal power series. Subtracting the surplus orbit contributes the multiplicative factor \(1-t^{k+1}\), giving the asserted zeta formula.

**4. Growth and fixed-point freeness.** The graph is strongly connected and has loops of lengths two and three, so \(A_k\) is primitive. Its positive Perron eigenvalue \(\beta_k\) obeys \(S_k(\beta_k^{-1})=1\): this follows from the same two-hub reduction and positivity. The equation has a unique solution above one by strict monotonicity. Perron–Frobenius gives \(\operatorname{tr}(A_k^n)=\beta_k^n(1+o(1))\); subtraction of a uniformly bounded endpoint correction does not alter the exponential rate. The equation \(\beta_k-1=1-\beta_k^{-k}\) also implies \(\beta_k\uparrow2\). Finally, an outer branch differs from the identity by \(\pm1\), and the formal fixed points of the two inner affine branches, \(\pm k/(k-1)\), lie outside their respective unit domains. Thus no fixed point exists.

## Verification

The included `verify.py` is a standalone standard-library program. It builds the transition graph, enumerates every closed admissible word up to period ten for each \(k=2,3,4,5\), solves the associated affine fixed-point equation in exact rational arithmetic, tests the real half-open itinerary, and checks the correction formula. It passed 96 exact finite checks. This is a consistency test of the proof, **not** an exhaustive computational proof for all periods or all integer gains. The symbolic determinant and endpoint coding arguments above establish the infinite conclusions.

## Relationship to prior work

García-Grimaldo and Campos-Cantón (2021) introduced the four-branch fixed-point-free system and analyzed fixed-point conditions, positive Lyapunov exponents, and Devaney chaos for a selected parameter. García-Grimaldo and collaborators (2023) presented the full piecewise formula, an FPGA realization, and bifurcation/Lyapunov plots over a range including outer slope one. The present exact all-period rational zeta, the correction for the jump orbit, and the integer-gain multinacci growth law are distinct from those numerical dynamics and fixed-point results. The 2022 comparative chapter by the originating authors discusses numerical entropy comparisons, but its complete text could not be inspected, leaving a priority risk. The same is true of the inaccessible complete text of the original 2021 journal article. Classical finite-state symbolic dynamics supplies the determinant method; that method alone does not identify the present specific Markov coding and its boundary correction.

## Limitations

This is a sharply defined **integer-gain, unit-outer-slope subfamily** and not a result for arbitrary real gains or outer slopes. The discontinuity at zero matters: replacing a half-open convention by a two-valued boundary relation changes the periodic orbit count. The symbolic entropy is stated for the explicitly constructed Markov partition; it is not claimed to be an automatically canonical topological entropy for every discontinuous-map convention. Full-text priority exclusion against the originating 2021 article and the 2022 comparative chapter was not possible. No independent mathematical audit has been performed.

## References

1. C. García-Grimaldo and E. Campos, “Chaotic Features of a Class of Discrete Maps without Fixed Points,” *International Journal of Bifurcation and Chaos* **31** (2021), 2150200. DOI: 10.1142/S021812742150200X. Public-record date: 2021-10-26.
2. C. García-Grimaldo, C. F. Bermudez-Marquez, E. Tlelo-Cuautle and E. Campos-Cantón, “FPGA Implementation of a Chaotic Map with No Fixed Point,” *Electronics* **12** (2023), 444. DOI: 10.3390/electronics12020444, open repository PDF: https://repositorio.ipicyt.edu.mx/bitstream/handle/11627/6542/Electronics12%282023%29444.pdf?isAllowed=y&sequence=1.
3. C. García-Grimaldo and E. Campos-Cantón, “Comparative Analysis of Chaotic Features of Maps Without Fixed Points,” in *Complex Systems and Their Applications* (2022), pp. 151–176. DOI: 10.1007/978-3-031-02472-6_8.

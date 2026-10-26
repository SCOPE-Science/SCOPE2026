# Exact two-total-domatic colouring counts of cycle prisms

## Finding

For every integer \(n\ge3\), consider \(P_n=C_n\square K_2\), with vertices \(u_i,v_i\) for \(i\in\mathbb Z/n\mathbb Z\), rail edges \(u_iu_{i+1},v_iv_{i+1}\), and rung edges \(u_iv_i\). A named two-colouring \(c:V(P_n)\to\{0,1\}\) is **two-total-domatic** when each *open* neighbourhood contains both colours. Let \(A_n\) be the number of such colourings. Define Lucas numbers by \(L_0=2\), \(L_1=1\), and \(L_{j+2}=L_{j+1}+L_j\) for \(j\ge0\). Then

\[
A_n=\begin{cases}
L_{2n}+6+4L_n,&n\equiv0\pmod 6,\\
L_{2n}+3-2L_n,&n\equiv2,4\pmod 6,\\
L_{2n}+2,&n\equiv3\pmod 6,\\
L_{2n}-1,&n\equiv1,5\pmod 6.
\end{cases}
\]

Global exchange of the two colours acts freely, so there are exactly \(A_n/2\) unordered partitions into two nonempty total dominating sets. For example \(A_3=20\), \(A_4=36\), \(A_5=122\), \(A_6=400\), and \(A_9=5780\).

## Assumptions and scope

Only simple cycle prisms with \(n\ge3\) are counted. The upper and lower vertex labels, all cycle positions, and the two colour names are fixed in \(A_n\): neither graph automorphisms nor rotation/reflection nor rung exchange is factored out. An unordered *partition* identifies only a global exchange of the two colour names. The condition uses open neighbourhoods, so no colour assigned to a vertex counts as a neighbour of that same vertex. The two classes are total dominating sets because every vertex has a neighbour in each class. This is a fixed two-class enumeration, not a claim about the maximum number of classes in a total domatic partition.

## Proof

**Step 1 — Local encoding.** Encode the two colours on rung \(i\) by \(s_i=(a_i,b_i)\in\{0,1\}^2\), with \(a_i=c(u_i)\), \(b_i=c(v_i)\), and identify this with the integers \(0,1,2,3\) in the fixed order \((0,0),(0,1),(1,0),(1,1)\). The required condition at rung \(i\) is precisely

\[
\bigl|\{a_{i-1},a_{i+1},b_i\}\bigr|=2,
\qquad
\bigl|\{b_{i-1},b_{i+1},a_i\}\bigr|=2.
\]

**Step 2 — Transfer and bijection.** Index a \(16\times16\) integer matrix \(T\) by ordered pairs of rung states. For states \(p,c,d,q\in\{0,1,2,3\}\), define \(T_{(p,c),(d,q)}=1\) exactly when \(c=d\) and both displayed local conditions hold with the predecessor \(p\), centre \(c\), and successor \(q\); otherwise the entry is zero. Every cyclic word \(s_0,\ldots,s_{n-1}\) produces exactly one closed walk \((s_{i-1},s_i)\to(s_i,s_{i+1})\) of length \(n\) in this transfer, and every such closed walk produces one cyclic word. The graph's neighbourhood constraints match the transfer's local conditions, including the triangular-prism boundary \(n=3\). Therefore

\[
A_n=\operatorname{tr}(T^n).
\]

**Step 3 — Exact characteristic polynomial.** Direct exact-integer determinant expansion (reproducible via the standalone Faddeev–LeVerrier/Cayley–Hamilton checker) gives

\[
\begin{aligned}
\det(xI-T)={}&(x-1)^2(x+1)^2(x^2-3x+1)(x^2+x+1)\\
&\quad\cdot(x^4-x^3+2x^2+x+1)\\
&\quad\cdot(x^4+x^3+2x^2-x+1).
\end{aligned}
\]

Put \(\varphi=(1+\sqrt5)/2\) and \(\psi=\varphi^{-1}\). The quadratic \(x^2-3x+1\) has roots \(\varphi^2,\psi^2\). The cubic-root factor \(x^2+x+1\) has roots \(\exp(\pm2\pi i/3)\). The remaining quartic factors are identically

\[
\begin{aligned}
x^4-x^3+2x^2+x+1&=(x^2-\varphi x+\varphi^2)(x^2+\psi x+\psi^2),\\
x^4+x^3+2x^2-x+1&=(x^2+\varphi x+\varphi^2)(x^2-\psi x+\psi^2).
\end{aligned}
\]

Thus their roots comprise \(\varphi\exp(\pm\pi i/3)\), \(\varphi\exp(\pm2\pi i/3)\), \(\psi\exp(\pm\pi i/3)\), and \(\psi\exp(\pm2\pi i/3)\). Trace of an integer power equals the sum of the corresponding eigenvalue powers *with algebraic multiplicities*, without any diagonalizability assumption. Hence

\[
\begin{aligned}
A_n={}&\varphi^{2n}+\psi^{2n}+2+2(-1)^n+2\cos(2\pi n/3)\\
&+2(\varphi^n+\psi^n)\bigl(\cos(\pi n/3)+\cos(2\pi n/3)\bigr).
\end{aligned}
\]

The cosine bracket vanishes for odd \(n\), is \(2\) if \(6\mid n\), and is \(-1\) for the other even residues modulo six. Moreover, \(\varphi^{2n}+\psi^{2n}=L_{2n}\), and \(\varphi^n+\psi^n=L_n\) for even \(n\). Separating the six residue classes proves the asserted formula.

**Step 4 — Unordered partitions.** Every admissible colouring uses both colours: each of its nonempty open neighbourhoods contains both. The global colour swap is fixed-point-free and its orbits correspond bijectively to unordered pairs of total dominating colour classes. Thus the partition number is \(A_n/2\). \(\square\)

## Verification

Run `python3 verify.py` in a directory containing only the embedded standalone files. It constructs the \(16\times16\) transfer by the displayed local predicate, computes the characteristic-polynomial coefficients by **integer-only** Faddeev–LeVerrier recurrence, checks them against the product of the six stated factors, and checks the Cayley–Hamilton identity. Independently, direct brute force inspects all \(2^{2n}\) labelled two-colourings for each integer \(3\le n\le9\). Transfer traces are compared to the claimed Lucas formula for every integer \(3\le n\le30\). The actual emitted results are recorded in `verification_output.txt`. These finite runs check the matrix computation and examples; the unrestricted \(n\ge3\) assertion follows from the transfer bijection and characteristic polynomial, not from extrapolation.

## Relationship to prior work

Asadzadeh and Alikhani, *Enumeration of total domatic partitions* (publicly uploaded 24 November 2025), give exact enumerations for several graph families, treat the five-prism among cubic graphs of order ten for its total-domatic number, and explicitly raise enumeration for Cartesian products of a graph and \(P_2\). Their prism discussion does not count its two-class partitions as a function of its cycle length. Rotenberg, Rutschmann, and Thomassen, *Disjoint Total Dominating Sets in Planar Graphs* (30 March 2026), prove existence of a two-total-domatic colouring for planar graphs of minimum degree at least three; existence gives no six-class enumerator. The present result solves the precise *two-class counting* case for \(C_n\square K_2\), not the general Cartesian-product enumeration or the maximum-partition count for those orders where three classes may be possible. The earlier 2017 Desormeaux–Haynes–Henning paper on partitioning cubic graphs into two total dominating sets was accessible only by its abstract; its possible relevance to counting is a residual historical-priority risk.

## Limitations

No statement is made about graphs beyond cycle prisms, graph-automorphism orbit counts, counting partitions into three or more total dominating classes, or the general maximal total-domatic number. A search of currently accessible research literature and published mathematical research records found no exact equivalent of this six-residue enumeration but cannot certify historical uniqueness. The inaccessible 2017 full text remains an explicit comparison limitation. Reproducible finite counts are corroboration only; they are not the proof for all \(n\).

## References

1. P. Asadzadeh and S. Alikhani, *Enumeration of total domatic partitions*, publicly available preprint, uploaded 24 November 2025. DOI: `10.13140/RG.2.2.25496.25607`. https://www.researchgate.net/publication/397926836_Enumeration_of_total_domatic_partitions
2. E. Rotenberg, D. Rutschmann, and C. Thomassen, *Disjoint Total Dominating Sets in Planar Graphs*, *Journal of Graph Theory* (first published 30 March 2026). DOI: `10.1002/jgt.70032`. https://onlinelibrary.wiley.com/doi/full/10.1002/jgt.70032
3. W. J. Desormeaux, T. W. Haynes, and M. A. Henning, *Partitioning the vertices of a cubic graph into two total dominating sets*, *Discrete Applied Mathematics* (2017). DOI: `10.1016/j.dam.2017.01.032`. Only the abstract was available in this comparison.

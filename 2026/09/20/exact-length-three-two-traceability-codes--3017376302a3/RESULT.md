# Exact maximum size of q-ary 2-traceability codes of length three

## Result

Let \(M_{\mathrm{TA}}(3,q,2)\) denote the maximum cardinality of a q-ary 2-traceability code of length three. Then, for every integer \(q\ge 2\),

\[
\boxed{M_{\mathrm{TA}}(3,q,2)=\max\left\{q,\left\lfloor\frac{3q-3}{2}\right\rfloor\right\}.}
\]

Equivalently,

\[
M_{\mathrm{TA}}(3,q,2)=
\begin{cases}
q,&q=2,3,4,\\[2mm]
\dfrac{3q-3}{2},&q\ge5\text{ odd},\\[2mm]
\dfrac{3q-4}{2},&q\ge6\text{ even}.
\end{cases}
\]

Thus the asymptotically best leading constant at length three is exactly \(3/2\).
For odd \(q\), the lower bound is the length-three construction of Blackburn--Etzion--Ng; the theorem proves its optimality. For even \(q\ge6\), a matching construction of size \((3q-4)/2\) is given below.

## Definitions

Let \(Q\) be an alphabet of size \(q\), and let \(C\subseteq Q^3\). For \(P\subseteq C\), its descendant set is

\[
\operatorname{desc}(P)=\{w\in Q^3: \text{for each coordinate }i,\ w_i=x_i\text{ for some }x\in P\}.
\]

For \(w\in Q^3\), let \(N_C(w)\) be the set of codewords at minimum Hamming distance from \(w\). The code \(C\) is 2-traceability if for every \(P\subseteq C\) with \(|P|\le2\) and every \(w\in\operatorname{desc}(P)\), one has

\[
N_C(w)\subseteq P.
\]

## A fiber-privacy lemma

For a coordinate \(i\) and symbol \(a\), write

\[
B_i(a)=\{x\in C:x_i=a\}.
\]

**Lemma.** Suppose \(C\) is a 2-traceability code of length three and
\(2\le |B_i(a)|<|C|\). Then every codeword \(x\in B_i(a)\) has a globally unique symbol in each of the other two coordinates.

**Proof.** Fix distinct \(x,y\in B_i(a)\), and let \(j,k\) be the other coordinates. Choose \(z\in C\setminus B_i(a)\).

First suppose, toward a contradiction, that \(x_j=y_j\). If \(z_k=y_k\), then \(y\in\operatorname{desc}(\{x,z\})\): coordinates \(i,j\) are supplied by \(x\), and coordinate \(k\) by \(z\). Since \(y\notin\{x,z\}\), the descendant \(y\) itself has an outside codeword at distance zero, contradicting 2-traceability.

If instead \(z_k\ne y_k\), form \(w\) by taking coordinates \(i,j\) from \(y\) and coordinate \(k\) from \(z\). Then \(w\in\operatorname{desc}(\{y,z\})\), \(d(w,y)=1\), and \(d(w,z)\ge1\) because \(z_i\ne a=w_i\). Meanwhile \(x\) agrees with \(w\) in coordinates \(i,j\), so \(d(w,x)\le1\). Hence the outside codeword \(x\) is at least as close to \(w\) as the nearest parent, again contradicting 2-traceability. Therefore distinct members of \(B_i(a)\) have distinct symbols in coordinate \(j\); similarly in coordinate \(k\).

It remains to exclude reuse by a codeword outside the fiber. Suppose \(u\notin B_i(a)\) satisfies \(u_j=x_j\). Choose \(y\in B_i(a)\setminus\{x\}\). From the preceding paragraph, \(y_j\ne x_j\). Let \(w\) take coordinate \(i\) from \(y\), coordinate \(j\) from \(u\), and coordinate \(k\) from \(y\). Then \(w\in\operatorname{desc}(\{y,u\})\), \(d(w,y)=1\), and \(d(w,u)\ge1\) because \(u_i\ne a=w_i\). But \(x\) agrees with \(w\) in coordinates \(i,j\), so \(d(w,x)\le1\). Thus the outside codeword \(x\) again lies among the nearest codewords, a contradiction. Hence \(x_j\) is globally unique. The same argument applies to coordinate \(k\). \(\square\)

## Upper bound

Let \(n=|C|\).

If some coordinate is constant on all codewords, then \(n\le q\). Indeed, in either other coordinate a proper non-singleton fiber would, by the lemma, force the constant-coordinate symbol to be globally unique for its members, impossible when \(n>1\). Hence each of the other coordinates is either constant or injective; because the codewords are distinct, at least one is injective, giving \(n\le q\).

Now assume no coordinate is constant. For coordinate \(i\), let \(R_i\) be the number of codewords lying in non-singleton fibers, and let \(G_i\) be the number of non-singleton fibers. Since every non-singleton fiber is proper, the lemma implies that a codeword belonging to a non-singleton fiber in one coordinate is singleton in each of the other two coordinates. Consequently

\[
R_1+R_2+R_3\le n.
\]

In coordinate \(i\), the number of distinct symbols actually used is

\[
(n-R_i)+G_i\le q,
\]

so

\[
R_i-G_i\ge n-q.
\]

If \(n\le q\), the desired bound is immediate. Suppose \(n>q\). Then every coordinate has at least one non-singleton fiber, so \(G_i\ge1\) for \(i=1,2,3\). Summing the previous inequalities gives

\[
3(n-q)\le \sum_{i=1}^3(R_i-G_i)
\le n-3.
\]

Therefore

\[
2n\le 3q-3,
\]

and hence

\[
n\le \left\lfloor\frac{3q-3}{2}\right\rfloor.
\]

Combining the two cases yields

\[
|C|\le \max\left\{q,\left\lfloor\frac{3q-3}{2}\right\rfloor\right\}.
\]

## Matching constructions

### The small-alphabet branch

For every \(q\), the diagonal code

\[
D_q=\{(a,a,a):a\in Q\}
\]

is 2-traceability and has size \(q\). For a descendant of at most two parents, one parent agrees in at least two coordinates, and every nonparent diagonal codeword disagrees in all three coordinates.

### The large-alphabet branch

Partition the codewords into three groups \(C_1,C_2,C_3\) of sizes \(a,b,c\). In coordinate \(i\), all codewords of \(C_i\) receive one common symbol, while every codeword outside \(C_i\) receives its own private symbol in that coordinate. This is feasible over a q-symbol alphabet whenever

\[
n-a+1\le q,\qquad n-b+1\le q,\qquad n-c+1\le q,
\]

where \(n=a+b+c\).

Every codeword then has two globally private coordinate symbols. If \(w\) is a descendant of one or two parents, one parent agrees with \(w\) in at least two coordinates, so the nearest-parent distance is at most one. Any outside codeword \(x\) at distance at most one from \(w\) would agree with \(w\) in at least two coordinates, one of which must be private for \(x\). But every coordinate of \(w\) is supplied by a parent, so that private symbol could only be supplied by \(x\) itself, contradicting that \(x\) is outside the parent set. Thus the construction is 2-traceability.

For \(q=2r+1\ge5\), take

\[
(a,b,c)=(r,r,r),
\]

giving \(n=3r=(3q-3)/2\). This is equivalent to the known Blackburn--Etzion--Ng length-three construction up to coordinatewise relabeling.

For \(q=2r\ge6\), take

\[
(a,b,c)=(r,r-1,r-1),
\]

giving

\[
n=3r-2=\frac{3q-4}{2}.
\]

Together with the upper bound, these constructions prove the theorem.

## Verification artifact

`artifacts/verify.py` constructs the stated codes for \(2\le q\le30\) and directly checks the 2-traceability definition for every parent set of size one or two and every descendant. The corresponding exact output is recorded in `artifacts/verification_output.txt`. These finite checks support the constructions; the upper bound is proved above and does not depend on computation.

## Relation to prior literature and originality

Blackburn, Etzion and Ng introduced the length-three odd-alphabet construction of size \(3(q-1)/2\) in their 2010 paper *Traceability Codes*. Owen and Ng (2015) reproduced that construction and stated that the best possible constant in the general 2-traceability upper bound was not known; their new upper-bound result concerned length four. Chen and Chen (2023) later determined optimal 2-traceability codes of length four. Chang and Hsu (2026) describe cardinalities of traceability codes as still unknown in broad generality and develop upper bounds for strengths three and four.

Searches through the present for exact length-three 2-traceability cardinalities, including synonymous `2-TA` notation and formula variants, did not locate the exact expression proved here. To the best of our knowledge, the exact all-q formula, the matching even-q construction, and the fiber-privacy upper-bound argument are not previously published. The principal residual originality risk is an older paper, thesis, or survey stating the same length-three result under different notation or as an unstated special case of a more general theorem.

## Limitations

The theorem is specific to strength two and length three. It does not determine \(M_{\mathrm{TA}}(n,q,2)\) for larger lengths or the corresponding exact capacities for strength at least three. The originality assessment is necessarily literature-dependent and is stated only to the best of our knowledge.

## References

1. S. R. Blackburn, T. Etzion, S.-L. Ng, “Traceability Codes,” *Journal of Combinatorial Theory, Series A* 117(8) (2010), 1049–1057. DOI: https://doi.org/10.1016/j.jcta.2010.02.009
2. S. Owen, S.-L. Ng, “A note on an upper bound of traceability codes,” *Australasian Journal of Combinatorics* 62(1) (2015), 140–146. https://ajc.maths.uq.edu.au/pdf/62/ajc_v62_p140.pdf
3. G. A. Kabatiansky, “Traceability Codes and Their Generalizations,” *Problems of Information Transmission* 55(3) (2019), 283–294. DOI: https://doi.org/10.1134/S0032946019030074
4. H.-B. Chen, G.-Y. Chen, “Optimal 2-traceability codes of length 4,” *Theoretical Computer Science* 954 (2023), 113800. DOI: https://doi.org/10.1016/j.tcs.2023.113800
5. H. Chang, C.-C. Hsu, “Lemmas on traceability codes and an upper bound for 4-traceability,” *Designs, Codes and Cryptography* 94(1) (2026), article 7. DOI: https://doi.org/10.1007/s10623-025-01748-z

# Superexponentially decaying colour budgets can avoid monochromatic triangles

## Finding

There is a positive nonincreasing sequence \(a=(a_i)_{i\ge1}\) with \(\sum_{i\ge1}a_i>1\) such that

\[
\log a_i=-\left(\frac18+o(1)\right)i\log i,
\]

and for infinitely many integers \(N\), the edges of \(K_N\) can be coloured so that colour \(i\) appears on at most \(a_i\binom N2\) edges and no triangle is monochromatic. In particular, \(a\not\to K_3\). This answers affirmatively the explicit question about sequences \(a_i=i^{-\Omega(i)}\) posed in *Decay-Ramsey Sequences*.

## Assumptions and scope

Write \(R_j(3)\) for the least order such that every edge-colouring of a complete graph with \(j\) colours contains a monochromatic triangle. We use the published lower bound \(R_j(3)\ge j^{j/3-o(j)}\); therefore, for all sufficiently large \(j\), a \(j\)-colouring of \(K_{\lfloor j^{j/4}\rfloor}\) with no monochromatic triangle exists. Fix an integer \(j_0\) for which this holds for every \(j\ge j_0\). For \(j<j_0\), put \(m_j=2\); for \(j\ge j_0\), put \(m_j=\lfloor j^{j/4}\rfloor\). For each \(j\), fix a colouring \(\chi_j:E(K_{m_j})\to[j]\) without a monochromatic triangle.

Set \(C_0=0\), \(C_j=\sum_{h=1}^j h=j(j+1)/2\), \(P_0=1\), and \(P_j=\prod_{h=1}^j m_h\). Define the sequence by

\[
a_i=\frac{2}{P_{j-1}}\qquad\text{whenever }C_{j-1}<i\le C_j.
\]

It is constant on each block of length \(j\), and the next block is smaller by a factor of \(m_j\ge2\). Thus it is positive and nonincreasing, with \(a_1=2\), so \(\sum_i a_i>1\).

## Proof

Fix a positive integer \(L\), and put \(N_L=P_L\). Identify the vertices of \(K_{N_L}\) with tuples \(x=(x_1,\ldots,x_L)\), where \(x_j\in[m_j]\). For distinct tuples \(x,y\), let \(j\) be the first coordinate where \(x_j\ne y_j\), and give the edge \(xy\) colour \(C_{j-1}+\chi_j(x_jy_j)\).

This colouring has no monochromatic triangle. Indeed, for any three distinct tuples, let \(j\) be the first coordinate at which their three entries are not all equal. If the three entries are distinct, all three edge-colours come from block \(j\), and their local colours form a triangle in \(\chi_j\), which is not monochromatic. If exactly two entries are equal, the edge joining the corresponding two tuples first differs at a later coordinate; its colour is therefore in a later block than the other two edges. Again the triangle is not monochromatic.

It remains to check the edge-density constraint. Fix a colour \(i=C_{j-1}+c\) in block \(j\), and put \(Q_j=\prod_{h=j+1}^{L}m_h\), with an empty product equal to \(1\). If \(e_{j,c}\) is the number of edges of colour \(c\) in \(\chi_j\), then the global colour class has exactly \(P_{j-1}e_{j,c}Q_j^2\) edges: choose a prefix, a base edge of colour \(c\), and independently choose the two suffixes. Since \(e_{j,c}\le\binom{m_j}{2}\) and \(N_L=P_{j-1}m_jQ_j\),

\[
\frac{e_i}{\binom{N_L}{2}}
\le \frac{m_j-1}{P_{j-1}m_j}\,\frac{N_L}{N_L-1}
<\frac{2}{P_{j-1}}=a_i.
\]

The strict inequality follows from \(N_L\ge2\), hence \(N_L/(N_L-1)\le2\), and \(m_j-1<m_j\). Thus the colouring is \(a\)-bounded. Because \(N_L\ge2^L\), these orders are unbounded, so \(a\not\to K_3\).

Finally, for all sufficiently large \(h\), \(\log m_h=(h/4)\log h+o(1)\). Hence

\[
\log P_{j-1}=\frac14\sum_{h<j}h\log h+O(1)
=\frac18j^2\log j+O(j^2).
\]

For \(C_{j-1}<i\le C_j\), we have \(i=j^2/2+O(j)\), and therefore \(i\log i=j^2\log j+O(j^2)\). Since \(\log a_i=\log2-\log P_{j-1}\), it follows that

\[
\log a_i=-\left(\frac18+o(1)\right)i\log i,
\]

or equivalently \(a_i=i^{-(1/8+o(1))i}\). In particular, \(a_i\le i^{-c i}\) eventually for every fixed \(c<1/8\).

## Verification

The proof uses the Ramsey lower bound only to guarantee the existence of the base colourings \(\chi_j\). The product construction, colour-class count, triangle check, and asymptotic block-index calculation are given explicitly above. No finite experiment is used as a substitute for the infinite statement. The construction is existential: it does not provide an explicit numerical value of \(j_0\) or explicit base colourings for all large \(j\).

## Relationship to prior work

Di Braccio, Griffiths, Noohi, and Versteegen explicitly ask whether a sequence with \(a_i=i^{-\Omega(i)}\) can fail to force a monochromatic triangle. Their Lemma 5.1 gives a product colouring from a single fixed \(r\)-colouring of \(K_m\), yielding an exponential budget of the form \(m^{1-i/r}\); their Proposition 1.5 consequently handles arbitrarily fast fixed exponential decay, not the superexponential scale considered here. The present construction varies both the palette size and the base order by block: block \(j\) uses \(j\) colours on a base graph of order about \(j^{j/4}\), while the density budget is controlled by the product of all preceding base orders. The multicolour Ramsey lower bound stated by Steiner supplies the required base colourings. The checked sources do not state this variable-block conclusion.

## Limitations

This is an existence result and does not characterize which superexponentially decaying sequences are Decay-Ramsey. The constant \(1/8\) is the exponent produced by this choice of block lengths and base orders; no optimality claim is made. Absolute priority cannot be proved by a bounded database search, and later or unindexed work remains a residual possibility.

## References

1. F. Di Braccio, S. Griffiths, P. Noohi, and L. Versteegen, “Decay-Ramsey Sequences,” arXiv:2610.20577, submitted 14 October 2026. https://arxiv.org/abs/2610.20577
2. R. Steiner, “Multicolor Ramsey numbers of odd cycles are superexponential,” arXiv:2608.02537, submitted 3 August 2026, §1. https://arxiv.org/abs/2608.02537

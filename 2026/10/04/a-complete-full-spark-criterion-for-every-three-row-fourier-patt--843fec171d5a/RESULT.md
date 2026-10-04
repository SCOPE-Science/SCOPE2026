# A complete full-spark criterion for every three-row Fourier pattern \(\{0,1,m\}\)
## Finding
For integers \(N\ge 3\) and \(2\le m\le N-1\), let \(F_N=(\omega^{rs})_{r,s\in\mathbb Z_N}\) with \(\omega=e^{-2\pi i/N}\), and select the three rows \(\mathcal M=\{0,1,m\}\). The resulting \(3\times N\) harmonic frame is full spark if and only if \(\gcd(N,m)\le 2\) and \(\gcd(N,m-1)\le 2\); equivalently, it is full spark if and only if \(\mathcal M\) is uniformly distributed over every divisor of \(N\).

Thus a natural two-parameter family of nonconsecutive three-row Fourier frames has a complete composite-order classification. In this family the divisor-uniformity condition, known to be necessary in general, is also sufficient for every Fourier order.

## Assumptions and scope
The parameters satisfy \(N\ge3\) and \(2\le m\le N-1\), so \(0,1,m\) are distinct residues modulo \(N\). Full spark means that every three selected columns are linearly independent. Replacing \(\omega\) by its complex conjugate does not change whether a minor vanishes.

## Proof
Choose three distinct columns whose corresponding \(N\)-th roots of unity are \(x,y,z\). Multiplying the columns by nonzero powers of \(x\) does not affect singularity, so after normalizing by \(x\) set \(u=y/x\) and \(v=z/x\). Then \(u,v\) are distinct \(N\)-th roots, neither equal to \(1\). Define
\[
S_m(t)=1+t+\cdots+t^{m-1}.
\]
A direct determinant calculation gives
\[
D:=\det\begin{{pmatrix}}1&1&1\\1&u&v\\1&u^m&v^m\end{{pmatrix}}
=-(u-1)(v-1)\bigl(S_m(u)-S_m(v)\bigr).
\]
Since \(u,v\ne1\), the minor is singular exactly when \(S_m(u)=S_m(v)=s\).

Because \(|u|=|v|=1\), conjugation gives
\[
\overline{{S_m(u)}}=u^{{1-m}}S_m(u),\qquad
\overline{{S_m(v)}}=v^{{1-m}}S_m(v).
\]
If \(s=0\), then the geometric-sum formula and \(u,v\ne1\) give \(u^m=v^m=1\). Hence \(1,u,v\) are three distinct common \(N\)-th and \(m\)-th roots of unity, so \(\gcd(N,m)\ge3\).

Now suppose \(s\ne0\). Equality of the conjugates implies \(u^{{m-1}}=v^{{m-1}}=:a\). Using the geometric-sum formula,
\[
S_m(u)=\frac{{a u-1}}{{u-1}},\qquad S_m(v)=\frac{{a v-1}}{{v-1}}.
\]
Equating these expressions and cross-multiplying yields
\[
(1-a)(u-v)=0.
\]
Since \(u\ne v\), one has \(a=1\). Thus \(1,u,v\) are three distinct common \(N\)-th and \(m-1\)-st roots, so \(\gcd(N,m-1)\ge3\).

This proves that any singular three-column minor forces at least one of the two gcds to be at least \(3\). Conversely, if \(g=\gcd(N,m)\ge3\), choose three distinct elements of the common subgroup of \(N\)-th and \(m\)-th roots. On those columns row \(m\) equals row \(0\), so the minor is singular. If instead \(g=\gcd(N,m-1)\ge3\), choose three distinct elements of the common subgroup of \(N\)-th and \(m-1\)-st roots; there row \(m\) equals row \(1\). Therefore the frame is full spark exactly when both gcds are at most \(2\).

For the divisor formulation, a three-element set is automatically uniformly distributed modulo \(1\), and \(\{{0,1,m\}}\) is always as balanced as possible modulo \(2\). For a divisor \(d\ge3\), uniform distribution of three residues is equivalent to their being pairwise distinct modulo \(d\). Since \(0\) and \(1\) are already distinct, failure occurs exactly when \(m\equiv0\pmod d\) or \(m\equiv1\pmod d\). Such a divisor \(d\ge3\) of \(N\) exists exactly when \(\gcd(N,m)\ge3\) or \(\gcd(N,m-1)\ge3\). This proves the equivalent formulation.

## Verification
The accompanying `verify_three_row_family.py` uses exact integer polynomial arithmetic to verify
\[
D=-(u-1)(v-1)(S_m(u)-S_m(v))
\]
for every \(2\le m\le60\). It also checks, with exact integer residue counts, the equivalence between the gcd criterion and divisor-uniformity for all \(3\le N\le300\) and \(2\le m<N\), totaling \(44,551\) parameter pairs. Finally it constructs exact singularity witnesses in every failing case through \(N=150\), totaling \(4,654\) witness cases. The replay prints `VERIFY_OK`. These finite checks are regression tests; the infinite theorem follows from the proof above, not extrapolation.

## Relationship to prior work
Alexeev, Cahill, and Mixon prove that uniform distribution over every divisor is necessary for an arbitrary row-selected DFT submatrix to be full spark, and sufficient when \(N\) is a prime power. They explicitly state that they do not have a characterization for a general DFT and exhibit a composite-order counterexample to general sufficiency. Their paper mentions \(\{{0,1,4\}}\) only to illustrate that uniform distribution modulo \(2\) and modulo \(4\) differ; it does not state the two-parameter criterion above.

Achanta et al. study full-spark Fourier sampling through coprimeness and vanishing sums. Their exact arithmetic-progression theorem concerns equally spaced rows, while their main nonconsecutive family deletes a single row from a consecutive block. The paper states that its general one-row-deletion conditions do not give a necessary-and-sufficient criterion for all parameters. Except for small boundary cases, \(\{{0,1,m\}}\) with \(m>3\) is neither an arithmetic progression nor a single-row deletion from a consecutive block, so those results do not imply the theorem here.

The result also strictly extends the previously established fixed-pattern case \(\{{0,1,4\}}\): setting \(m=4\) gives the sharp condition \(3\nmid N\) and \(4\nmid N\).

## Limitations
The theorem classifies exactly the three-row family \(\{{0,1,m\}}\); it does not classify arbitrary three-row subsets up to affine equivalence, nor larger row sets. The originality check used targeted published-finding corpus searches plus full-text inspection of the two most relevant primary sources, but a differently phrased or poorly indexed earlier statement may exist. The later journal continuation of the coprimeness program was compared at the metadata/abstract level rather than by direct full-text inspection.

## References
1. B. Alexeev, J. Cahill, D. G. Mixon, *Full Spark Frames*, arXiv:1110.3548 (first posted 2011-10-17), later J. Fourier Anal. Appl. 18 (2012), 1167–1194.
2. H. K. Achanta, S. Biswas, S. Dasgupta, M. Jacob, B. N. Dasgupta, R. Mudumbai, *Coprime Conditions for Fourier Sampling for Sparse Recovery*, IEEE SAM 2014, DOI: 10.1109/SAM.2014.6882460.

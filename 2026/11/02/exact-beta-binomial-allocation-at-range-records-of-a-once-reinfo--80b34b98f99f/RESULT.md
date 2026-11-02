# Exact beta-binomial allocation at range records of a once-reinforced random walk

## Finding
For symmetric once-reinforced nearest-neighbour random walk on the integer line with any reinforcement weight \(c>0\), let \(S_k\) be the first instant at which the explored interval has length \(k\), and let \(J_k\) count expansions of its right endpoint through that instant. For all integers \(k\geq1\) and \(0\leq j\leq k\),
\[
\Pr(J_k=j)=\binom{k}{j}\frac{(c)_j(c)_{k-j}}{(2c)_k}.
\]
Here \((a)_0=1\) and \((a)_m=a(a+1)\cdots(a+m-1)\) for positive integers \(m\). This is exactly the symmetric beta-binomial law.

More sharply, writing \(E_k\in\{+,-\}\) for the side of the final (\(k\)-th) expansion,
\[
\Pr(J_k=j,E_k=+)=\frac{j}{k}\Pr(J_k=j),\qquad
\Pr(J_k=j,E_k=-)=\frac{k-j}{k}\Pr(J_k=j).
\]
Thus the conditional probability that the last record was on the right, given exactly \(j\) right records, is \(j/k\), independently of \(c\).

Despite these beta-binomial count marginals, the expansion-sign sequence is **not exchangeable** for any finite \(c>0\). Its first three signs satisfy
\[
\frac{\Pr(E_1=+,E_2=+,E_3=-)}{\Pr(E_1=+,E_2=-,E_3=+)}=\frac{1+c}{c}>1.
\]
In particular,
\[
\mathbb E[J_k]=\frac{k}{2},\qquad
\operatorname{Var}(J_k)=\frac{k(k+2c)}{4(2c+1)},\qquad
\frac{J_k}{k}\Rightarrow\operatorname{Beta}(c,c).
\]
The weak convergence is of one-dimensional distributions at successive range records; the theorem does not assert an almost-sure limit of the same sequence.

## Assumptions and scope
Fix \(c>0\). Start at \(X_0=0\) on \(\mathbb Z\). Each edge initially carries weight \(1\), changed permanently to \(c\) after its first traversal. At each step the walk chooses one of its two neighbouring edges with probability proportional to its present weight. Put \(M_n=\max_{0\leq t\leq n}X_t\), \(m_n=\min_{0\leq t\leq n}X_t\), \(R_n=M_n-m_n\), and \(S_k=\inf\{n:R_n=k\}\). There are no holding steps, so each range expansion increases \(R_n\) by exactly one. At \(S_k\), the walk stands at the newly discovered endpoint. Set \(J_k=M_{S_k}\) and \(E_k=+\) when the most recent expansion is on the positive side and \(E_k=-\) otherwise. Every \(S_k\) is almost surely finite by absorption of the recurrent finite-interval nearest-neighbour chain at its two accessible outside edges.

## Proof
**1. Exact next-side law from the original walk.** Consider the interval \(\{0,1,\ldots,k\}\) already explored, and let \(h_j\) be the probability that the *next* expansion will be to \(k+1\) rather than \(-1\), conditional on currently standing at \(j\). All internal edges have weight \(c\), and the two unvisited outside edges have weight \(1\). First-step conditioning gives
\[
h_j=\tfrac12(h_{j-1}+h_{j+1})\quad(1\le j\le k-1),
\qquad h_0=\frac{c}{1+c}h_1,
\qquad h_k=\frac{1}{1+c}+\frac{c}{1+c}h_{k-1}.
\]
The unique solution, found by affineness in the interior, is
\[
h_j=\frac{j+c}{k+2c}\quad(0\le j\le k).
\]
After a new right-endpoint record, the walk is at \(k\); after a left-endpoint record it is at \(0\), up to spatial translation. The strong Markov property of the expanded-range state gives
\[
\Pr(E_{k+1}=E_k\mid E_1,\ldots,E_k)=\frac{k+c}{k+2c},
\qquad
\Pr(E_{k+1}\ne E_k\mid E_1,\ldots,E_k)=\frac{c}{k+2c}.
\]
In particular the right/left switch probability depends on the range level but not the previous record history.

**2. Joint induction.** Write
\[
B_k(j)=\binom{k}{j}\frac{(c)_j(c)_{k-j}}{(2c)_k},\qquad 0\le j\le k.
\]
At level one, \(\Pr(J_1=1,E_1=+)=\Pr(J_1=0,E_1=-)=1/2\); hence the two asserted joint identities hold. Suppose they hold at level \(k\), using \(B_k(j)=0\) outside \(0\le j\le k\). For \(1\le j\le k+1\), the next record is positive only if \(J_k=j-1\), and the next-side transition law yields
\[
\begin{aligned}
\Pr(J_{k+1}=j,E_{k+1}=+)
&=\frac{k+c}{k+2c}\frac{j-1}{k}B_k(j-1)
 +\frac{c}{k+2c}\frac{k-j+1}{k}B_k(j-1)\\
&=\frac{j-1+c}{k+2c}B_k(j-1)
=\frac{j}{k+1}B_{k+1}(j).
\end{aligned}
\]
The negative side follows by reflection, giving \(\Pr(J_{k+1}=j,E_{k+1}=-)=(k+1-j)B_{k+1}(j)/(k+1)\). Their sum gives the beta-binomial formula at the next level. All boundary cases follow by the zero convention.

**3. A nonexchangeable path with exchangeable-style counts.** The two paths of three record signs \((+,+,-)\) and \((+,-,+)\) both contain two positive records. The transition kernel gives respective probabilities
\[
\frac12\frac{1+c}{1+2c}\frac{c}{2+2c},
\qquad
\frac12\frac{c}{1+2c}\frac{c}{2+2c},
\]
which have ratio \((1+c)/c\). Thus the directions themselves cannot be an exchangeable Pólya-urn sequence even though their *count* distribution agrees with its symmetric beta-binomial count distribution.

**4. Consequences.** The beta-binomial law equals the mixture obtained by first sampling \(U\sim\operatorname{Beta}(c,c)\) and then a conditionally binomial \(\operatorname{Bin}(k,U)\) variable. This mixture representation is an identity in one-dimensional law, not a claim about a common latent variable driving the record directions. It yields the displayed exact mean and variance and, using conditional binomial concentration, \(J_k/k\Rightarrow U\).

## Verification
The accompanying standalone `check.py` operates with exact rational arithmetic for six weights \(c\in\{1/5,1/2,1,4/3,2,5\}\). It independently solves the original finite-state exit equations, propagates the record-side chain for 30 range levels, checks all joint beta-binomial probabilities and normalizations, verifies the moment formulas, and compares two nonexchangeable sign histories. Run `python3 check.py` with the Python standard library; `check_output.txt` records the reproduced output. The finite checks supplement, but do not replace, the algebraic proof for all \(c>0\) and all levels.

## Relationship to prior work
Hu, Ma, Song and Wang (arXiv:2602.10721, first public version February 11, 2026) obtain range-moment asymptotics for the *half-line* model with a reflecting boundary. Pfaffelhuber and Stiefel (arXiv:1903.05234) treat full-line range moments and describe how reinforcement changes the relative growth of the two extrema, but their inspected result does not state the finite-record beta-binomial allocation or the last-direction conditioning identity. The separate record-statistics literature, notably Serlet (2018), is a substantial priority caveat: the accessible abstract concerns explicit invariance principles for record signs and values; the full chapter was not accessible for a definitive comparison. A corresponding prior exact finite-record formula, if present there, would supersede the claimed originality. No novel claim is made for the classical beta-binomial distribution itself.

## Limitations
Only the symmetric, constant-weight once-reinforced nearest-neighbour walk on the full integer line is addressed. The law is indexed by *record count* rather than deterministic time; it does not specify the joint law of record count and record waiting times, nor the marginal distribution of the walk position at fixed time. The equality of beta-binomial *count* laws does not imply exchangeability of the directions, and the weak beta convergence does not establish pathwise convergence. The older Serlet record-law chapter was not fully inspected, so historical-priority risk remains material and warrants independent follow-up.

## References
- Z. Hu, T. Ma, R. Song and L. Wang, *The range of once-reinforced random walk on the half-line*, arXiv:2602.10721v1 (first publicly posted 2026-02-11), https://arxiv.org/abs/2602.10721 .
- P. Pfaffelhuber and J. Stiefel, *The range of once-reinforced random walk in one dimension*, arXiv:1903.05234v1 (2019), https://arxiv.org/abs/1903.05234 ; published in *Random Structures & Algorithms*, DOI:10.1002/rsa.20948.
- L. Serlet, *Explicit Laws for the Records of the Perturbed Random Walk on the Integer Line*, *Séminaire de Probabilités XLIX* (2018), DOI:10.1007/978-3-319-92420-5_14 (abstract inspected; full chapter inaccessible).

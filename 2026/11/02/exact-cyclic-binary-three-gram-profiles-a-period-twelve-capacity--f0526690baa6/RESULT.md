# Exact cyclic binary three-gram profiles: a period-twelve capacity quasipolynomial

## Finding

For every integer \(n\geq1\), let \(\mathcal W_n=\{0,1\}^n\), interpreted cyclically. For each \(w\in\mathcal W_n\), define its *ordered three-gram multiplicity profile* by
\[
\mathbf p_3(w)=(N_{000}(w),N_{001}(w),\ldots,N_{111}(w)),
\quad N_{abc}(w)=\bigl|\{i\in\mathbb Z/n\mathbb Z:(w_i,w_{i+1},w_{i+2})=(a,b,c)\}\bigr|.
\]
The same cyclic convention applies when \(n=1\) or \(n=2\): positions may recur within a length-three read. Let \(C_n=|\{\mathbf p_3(w):w\in\mathcal W_n\}|\). Define the periodic functions
\[
\tau_3(n)=\begin{cases}2&n\equiv0\pmod3,\\-1&\text{otherwise},\end{cases}
\qquad
\tau_4(n)=\begin{cases}1&n\equiv0\pmod4,\\-1&n\equiv2\pmod4,\\0&n\text{ odd}.\end{cases}
\]
Then the exact number of realizable ordered three-gram profiles is
\[
\boxed{C_n=\frac{6n^4+276n^2+3943}{1728}+\frac{19(-1)^n}{64}+\frac{\tau_4(n)}8+\frac{4\tau_3(n)}{27}}\quad(n\geq1).
\]
Equivalently, the ordinary generating function is
\[
\boxed{\sum_{n\geq1}C_nz^n=\frac{2z}{1-z}+\frac{z^2}{1-z^2}+\frac{2z^3}{(1-z)(1-z^2)(1-z^3)}+\frac{z^4(z^2-z+1)}{(1-z)^4(1-z^2)(1+z^2)(1+z+z^2)}}.
\]
The sequence \((C_1,\ldots,C_{19})\) is
\[
(2,3,4,6,8,13,18,27,38,53,72,98,128,167,214,271,338,419,512).
\]
The count is a degree-four quasipolynomial of **least period twelve**, and \(C_n\sim n^4/288\). Accordingly, if a noiseless observation returns exactly the multiset of \(n\) oriented cyclic three-letter reads, the largest zero-error length-\(n\) binary code with distinct observation profiles has precisely \(C_n\) codewords (one representative of each profile). The claim is about *profiles*, not the number of circular words and not injectivity on all words.

## Assumptions and scope

The binary alphabet is labeled, the reads are oriented, order within each three-letter read is retained, and their positions and order of presentation are discarded. Multiplicities are retained. Rotations of a word give the same observation but are not otherwise identified in defining the set of input linear representations. The profile vector coordinates correspond, in that order, to \(000,001,010,011,100,101,110,111\). The statement holds for all positive integer lengths, including the short circular conventions specified above; no aperiodicity assumption is imposed.

## Proof

**1. Balanced directed-edge characterization.** Use the binary order-two de Bruijn digraph, whose four vertices are \(00,01,10,11\), and whose eight directed edges are the triples \(abc\colon ab\longrightarrow bc\). For any cyclic word, its edge multiplicities form a nonnegative integer circulation with connected positive-edge support (after vertices of degree zero are discarded). Conversely, for any such circulation, the directed multigraph with the specified edge copies is Eulerian. A closed Euler trail yields a cyclic binary word with *exactly* those three-gram counts: labels of successive overlapping vertices prescribe the successive letters. Thus balance and positive-support connectedness are jointly necessary and sufficient.

Write
\[
a=N_{000},\quad b=N_{001}=N_{100},\quad c=N_{010},\quad d=N_{011}=N_{110},\quad f=N_{101},\quad h=N_{111}.
\]
The equalities for \(001/100\) and \(011/110\) follow from balance at \(00\) and \(11\), respectively. Balance at \(01\) (equivalently \(10\)) is the remaining equation
\[
\boxed{c+d=b+f},\qquad a,b,c,d,f,h\geq0,
\quad n=a+h+2b+c+2d+f.
\]
It remains essential to retain connectedness; simply counting nonnegative solutions of these linear equations overcounts disconnected supports.

**2. Exact support partition.** Split into four disjoint cases according to which of the bridge counts \(b,d\) are positive.

- If \(b=d=0\), balance gives \(c=f\). The only *connected* positive edge supports are the isolated loop at \(00\), the isolated loop at \(11\), and the connected directed \(01\leftrightarrow10\) two-cycle. Their respective lengths contribute \(2z/(1-z)+z^2/(1-z^2)\). A combination of these separate components cannot be realized by one cyclic word.
- If \(b>0,d=0\), the bridge edges and the \(010\) edge form the connected directed \(00\to01\to10\to00\) triangle, with \(c=b+f\), \(h=0\), and free \(a,f\geq0\). The total number of edges is \(n=a+3b+2f\). The generating function for this case is therefore \(z^3/((1-z)(1-z^2)(1-z^3))\). If \(b=0,d>0\), the symmetric case has \(a=0\), \(f=c+d\), and \(n=h+3d+2c\), giving an identical generating function.
- If \(b,d>0\), both pairs of bridge edges occur; their positive support already contains the directed four-cycle \(00\to01\to11\to10\to00\) when necessary, and is therefore connected. Set \(t=c+d=b+f\); then \(t\geq\max(b,d)\), \(c=t-d\), \(f=t-b\), and \(n=a+h+b+d+2t\). Both loop counts \(a,h\geq0\) are free. Thus the contribution is
\[
\frac1{(1-z)^2(1-z^2)}\sum_{b,d\geq1} z^{b+d+2\max(b,d)}.
\]
For \(m=\max(b,d)\), the diagonal \(b=d=m\) contributes \(z^{4m}\); the two off-diagonal choices contribute \(2\sum_{j=1}^{m-1}z^{3m+j}\). Summing the geometric series gives
\[
\sum_{b,d\geq1}z^{b+d+2\max(b,d)}
=\sum_{m\geq1}z^{4m}+2\sum_{m\geq2}\sum_{j=1}^{m-1}z^{3m+j}
=\frac{z^4(z^2-z+1)}{(1-z)^2(1+z^2)(1+z+z^2)}.
\]
Every parameter tuple in the four cases specifies one distinct profile, since its eight labeled coordinates recover all parameters. Each profile is realizable by the connected Eulerian argument from Step 1. Summing the four contributions proves the displayed rational generating function without omissions or double-counting.

**3. Coefficient extraction.** Elementary partial fractions give the exact identity
\[
\begin{aligned}
\sum_{n\geq1}C_nz^n={}&-3+\frac{4225}{1728(1-z)}-\frac{17}{32(1-z)^2}+\frac{71}{144(1-z)^3}\\
&-\frac5{24(1-z)^4}+\frac1{12(1-z)^5}+\frac{19}{64(1+z)}+\frac1{8(1+z^2)}+\frac{4(z+2)}{27(1+z+z^2)}.
\end{aligned}
\]
For \(n\geq1\), the sum of coefficients from poles at \(z=1\) simplifies to \((6n^4+276n^2+3943)/1728\). The terms at \(-1\), at the fourth roots \(\pm i\), and at the primitive cube roots contribute, respectively, \(19(-1)^n/64\), \(\tau_4(n)/8\), and \(4\tau_3(n)/27\). This proves the claimed formula, with exact integer values because the coefficients count profiles. The primitive third-root and fourth-root poles are both genuine (their numerators do not vanish there); consequently any quasipolynomial period must be divisible by both three and four. The displayed formula has period twelve, proving that this is the least period.

**4. Capacity interpretation.** Two binary length-\(n\) words are confusable under the deterministic circular three-read multiset channel precisely when they have equal profiles. Any zero-error code contains at most one word per profile, and choosing one representative from each nonempty profile class attains that bound. Its exact maximum cardinality is therefore \(C_n\).

## Verification

The accompanying dependency-free `verify.py` forms the literal eight-coordinate cyclic read multiset for every binary word at lengths \(1\) through \(18\), constructs the independent balance-and-connectedness parameterization, and checks both exact profile-set equality and the formula. For lengths \(19\) through \(46\), it independently enumerates the parameterized profile sets and checks the formula. The tested initial sequence matches the one above, with \(C_{12}=98\) and \(C_{24}=1247\). These finite checks corroborate the proof; the infinite theorem follows from the Eulerian support partition and generating-function identity, not from finite enumeration.

To reproduce: run `python3 verify.py` in the directory containing this document and the code. No external dependencies, solvers, or network connection are required.

## Relationship to prior work

Kiah, Puleo and Milenkovic's *Codes for DNA Sequence Profiles* develops general (including de Bruijn graph and Ehrhart) methods for string profile classes; its Table I gives the asymptotic leading coefficient \(c(2,3)=1/288\), consistent with the present formula, but does not state the exact all-length cyclic binary three-gram generating function or its period-twelve correction. Jacquet, Knessl and Szpankowski's *Counting Markov Types* treats order-one Markov types (adjacent-pair counts) and asymptotics, not the exact connected order-two binary type profile. Yehezkeally et al.'s *Generalized Unique Reconstruction from Substrings* treats reconstruction codes under longer or selectively observed substring models, not this finite exact cardinality. The related published binary cyclic two-read result counts *bigram* profiles, one level below the present problem. These general theories and neighboring special cases are acknowledged rather than claimed as new.

## Limitations

The statement applies only to the labeled binary alphabet, oriented cyclic reads of length exactly three, and multiplicity-preserving observation. It does not classify the size of each fiber or provide an explicit efficiently encodable optimal code. Independent scientific validation has not been performed. A differently phrased exact enumeration in older high-order Markov-type or DNA-profile literature may exist despite the identified comparisons.

## References

1. H. M. Kiah, G. J. Puleo, and O. Milenkovic, *Codes for DNA Sequence Profiles*, arXiv:1410.8837 (2014 preprint; relevant 2015 revised version), https://arxiv.org/html/1410.8837v2, Sections 2, 4–5, 7, Table I.
2. P. Jacquet, C. Knessl, and W. Szpankowski, *Counting Markov Types*, DMTCS Proceedings AM (2010), DOI: 10.46298/dmtcs.2768, https://www.cs.purdue.edu/homes/spa/papers/aofa10.pdf.
3. Y. Yehezkeally, D. Bar-Lev, S. Marcovich, and E. Yaakobi, *Generalized Unique Reconstruction from Substrings*, arXiv:2210.04471, first submitted October 10, 2022, https://arxiv.org/abs/2210.04471.
4. Published published-finding corpus record, *Exact binary two-multispectrum code size and singleton classification*, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-binary-two-multispectrum-code-size-and-singleton-classific--13779c08da71 (adjacent-pair, rather than length-three, cyclic profile counts).

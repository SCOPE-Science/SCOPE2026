# Sharp cyclic inverse-branching bound for elementary Rule 110

## Finding
For every integer \(n\geq1\), let \(F_n:\{0,1\}^n\to\{0,1\}^n\) be the synchronous binary elementary cellular automaton Rule 110 with periodic boundary conditions. For each indexed output \(y\), write \(d_n(y)=|F_n^{-1}(y)|\) and \(m=\sum_{i=0}^{n-1}y_i\). Define the Perrin numbers by \(P_0=3\), \(P_1=0\), \(P_2=2\), and \(P_j=P_{j-2}+P_{j-3}\) for all \(j\geq3\). Then
\[
0\leq d_n(y)\leq P_m.
\]
For every \(n\geq5\), the exact maximum inverse-fiber cardinality is
\[
\max_{y\in\{0,1\}^n}d_n(y)=P_n,
\]
and the **unique** maximizing indexed output is the constant-one configuration \(y=1^n\). Moreover \(d_n(0^n)=2\) for all \(n\geq1\), and every output with exactly one one has no predecessor.

## Assumptions and scope
The local update is \(f(a,b,c)=(110\mathbin{\mathrm{div}}2^{4a+2b+c})\bmod2\), for \(a,b,c\in\{0,1\}\); equivalently the triples with output one are \(001,010,011,101,110\). The successor coordinate is \((F_n(x))_i=f(x_{i-1},x_i,x_{i+1})\), with all indices reduced modulo \(n\). Configurations are indexed binary tuples; cyclic shifts are not identified, and the result includes the small rings \(n=1,2\) with repeated neighbor sites. The Perrin number \(P_0=3\) is the trace of an identity matrix, not a count of length-zero configurations.

## Proof
**1. A labeled three-state predecessor graph.** For each predecessor \(x\) and site \(i\), assign state \(A\) if \(x_i=0\), state \(B\) if \((x_{i-1},x_i)=(0,1)\), and state \(C\) if \((x_{i-1},x_i)=(1,1)\). The complete permitted state transitions, with the Rule-110 output label at site \(i\), are
\[
A\xrightarrow{0}A,\quad A\xrightarrow{1}B,\quad
B\xrightarrow{1}A,\quad B\xrightarrow{1}C,\quad
C\xrightarrow{1}A,\quad C\xrightarrow{0}C.
\]
For example, the edge \(B\to C\) corresponds to input triple \(011\), and \(C\to A\) to \(110\). Every indexed cyclic binary predecessor gives one closed path of length \(n\); conversely, a closed labeled path uniquely recovers \(x_i=0\) in state \(A\) and \(x_i=1\) in states \(B,C\), with the preceding bit fixed by the displayed transitions. Thus this is a bijection, including the short rings.

In state order \((A,B,C)\), the zero- and one-labeled adjacency matrices are
\[
T_0=\begin{pmatrix}1&0&0\\0&0&0\\0&0&1\end{pmatrix},\qquad
T_1=\begin{pmatrix}0&1&0\\1&0&1\\1&0&0\end{pmatrix}.
\]
Consequently the exact number of cyclic predecessors is
\[
d_n(y)=\operatorname{tr}(T_{y_0}T_{y_1}\cdots T_{y_{n-1}}).
\]

**2. The weight envelope.** Matrices are nonnegative entrywise and \(0\leq T_0\leq I_3\) entrywise. Replacing any occurrence of \(T_0\) in the product by \(I_3\) cannot decrease any matrix entry, hence cannot decrease its trace. Removing all \(n-m\) zero-labeled factors therefore gives
\[
d_n(y)\leq\operatorname{tr}(T_1^m).
\]
The characteristic identity \(T_1^3=T_1+I_3\) follows by direct multiplication. Hence the traces \(\operatorname{tr}(T_1^m)\) have the initial values \(3,0,2\) and obey the Perrin recurrence; they equal \(P_m\) for all \(m\geq0\). Equality holds for \(y=1^n\), for which no factors are replaced.

**3. Uniqueness and boundary indices.** The values \(P_0,\ldots,P_7\) are \(3,0,2,3,2,5,5,7\). For every \(j\geq4\), the recurrence implies \(P_{j+2}=P_j+P_{j-1}>P_j\). Thus \(P_{k}>P_{k-1}\) for all \(k\geq8\), since \(P_k-P_{k-1}=P_{k-2}-P_{k-4}=P_{k-5}>0\). With \(P_7>P_6\), it follows for all \(n\geq7\) that \(P_m<P_n\) whenever \(m<n\). At \(n=5\), every lower index also has \(P_m<P_5=5\). The sole remaining equality of a lower-index envelope occurs at \(n=6\), \(m=5\), since \(P_5=P_6=5\). All such outputs are cyclic rotations of one zero followed by five ones. For them cyclic trace invariance yields
\[
d_6(y)=\operatorname{tr}(T_0T_1^5)=P_5-(T_1^5)_{BB}=5-2=3<5=P_6,
\]
where direct matrix multiplication gives \((T_1^5)_{BB}=2\). Therefore the all-one output is the unique maximizer for every \(n\geq5\).

**4. Two immediate exact boundaries.** Since \(T_0^n=T_0\) for \(n\geq1\), we have \(d_n(0^n)=\operatorname{tr}(T_0)=2\). For any output with one one, the weight envelope gives \(0\leq d_n(y)\leq P_1=0\), proving nonexistence of predecessors. This completes the proof.

## Verification
The accompanying \(\texttt{verify\_rule110.py}\) independently evaluates Rule 110 directly from its eight-bit truth table and enumerates all indexed input configurations on rings of size \(1\) through \(13\). It checks the exact all-one fiber size, the two all-zero predecessors, the Perrin weight envelope and the unique maximum at every tested size at least five. It separately constructs the ordinary **four-state** de Bruijn transfer matrices from the truth table and checks their trace formula against direct enumeration for all outputs through ring size seven. Execution under Python 3 returns \(\texttt{VERIFY\_OK}\). These finite calculations are diagnostic checks; the preceding matrix argument proves the theorem for arbitrary length.

## Relationship to prior work
Jen's 1989 full-length study derives preimage recurrences for arbitrary output blocks on the infinite lattice and discusses which blocks maximize one-step preimage probability (Section 5.4); it does not state this finite-cyclic Perrin envelope and strict maximizing-fiber theorem. Powley and Stepney (2010) study preimages of **homogeneous** configurations on finite lattices using de Bruijn matrices; the count for the homogeneous-one Rule-110 output and the matrix method are established background, not claimed as discoveries here. Their reported scope does not settle the comparison with every inhomogeneous output. Powley's thesis also discusses heterogeneous periodic outputs; its complete text could not be inspected, so possible implicit coverage remains a priority risk. Fukś (2013 preprint, initially public 28 May 2013) studies higher-step preimage sequences of finite blocks, a distinct object. The independently established contribution here is the **all-target** Hamming-weight upper bound and the strict global optimum/uniqueness on cyclic rings for all lengths \(n\geq5\).

## Limitations
No result about higher preimage depths, stochastic perturbations, infinite nonperiodic configurations, or computational universality follows from this theorem. It does not claim the Perrin recurrence for the homogeneous target as new. Although the inspected sources do not state the full theorem, an older implicit comparison in unavailable primary literature cannot be ruled out; independent historical-priority assessment remains outstanding.

## References
- E. Jen, "Enumeration of Preimages in Cellular Automata," *Complex Systems* **3** (1989), 421–456, especially Sections 2 and 5.4. https://content.wolfram.com/sites/13/2018/02/03-5-2.pdf
- E. J. Powley and S. Stepney, "Counting Preimages of Homogeneous Configurations in 1-Dimensional Cellular Automata," *Journal of Cellular Automata* **5** (2010), 353–381. https://pure.york.ac.uk/portal/en/publications/counting-preimages-of-homogeneous-configurations-in-1-dimensional/
- E. J. Powley, *Preimages of homogeneous configurations*, PhD thesis, Chapter 9, University of York (2010). https://www.cs.york.ac.uk/nature/group/theses/EdPowley.pdf
- H. Fukś, "Sequences of preimages in elementary cellular automata," first arXiv version 28 May 2013, arXiv:1305.6533. https://arxiv.org/abs/1305.6533

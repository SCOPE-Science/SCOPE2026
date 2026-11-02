# Sharp cyclic one-step preimage rankings for Rule 54

## Finding
Let \(F_n:\{0,1\}^n\to\{0,1\}^n\) be the synchronous Rule-54 update on an *indexed cyclic ring* with \(n\ge8\). Write \(d_n(y)=|F_n^{-1}(y)|\). Let \(R_0=3,R_1=0,R_2=2\) be the Perrin sequence, let \(P_0=P_1=P_2=1\) be the Padovan sequence, and extend both by \(u_k=u_{k-2}+u_{k-3}\) for \(k\ge3\). Then

\[
 d_n(1^n)=R_n>P_{n-2}=\max_{y\ne 1^n} d_n(y).
\]

Equality in the right-hand maximization holds **exactly** for the \(n\) indexed words with a single cyclic adjacent pair of zeros and all other entries one, namely the cyclic rotations of \(00 1^{n-2}\). Thus \(1^n\) is the unique most frequent one-step output under uniformly chosen input, and there are precisely \(n\) second-most-frequent outputs.

## Assumptions and scope
All configurations have \(n\) indexed, cyclically adjacent binary sites. At each site the simultaneous update is \(f(a,b,c)=b\oplus(a\lor c)\), the standard Wolfram Rule 54, with neighbors indexed modulo \(n\). A preimage is counted as a labeled configuration; cyclic rotations are **not** quotiented. Exactly one update is performed. The statement concerns every integer \(n\ge8\), not an extrapolation from finite experiments.

## Proof

**Pair transfer matrices.** Order the pair states as \(00,01,10,11\). The adjacency matrices \(A\) and \(B\), for prescribed output bits zero and one respectively, are

\[
 A=\begin{pmatrix}1&0&0&0\\0&0&0&1\\0&0&0&0\\0&0&1&1\end{pmatrix},\qquad
 B=\begin{pmatrix}0&1&0&0\\0&0&1&0\\1&1&0&0\\0&0&0&0\end{pmatrix}.
\]

Every length-\(n\) predecessor corresponds bijectively to a closed length-\(n\) walk through these pair states, even for periodic inputs; therefore \(d_n(y)=\operatorname{tr}(T_{y_0}\cdots T_{y_{n-1}})\), where \(T_0=A,T_1=B\). Direct multiplication gives \(A^3=A^2=E\), \(B^4=B^2+B\), and the entrywise inequality \(B^3\ge BAB\). In particular, replacing an isolated output zero in a cyclic occurrence \(101\) by one (giving \(111\)) cannot decrease its fiber, whatever the surrounding output bits.

**Two-dimensional reduction.** Put

\[
 U=\begin{pmatrix}1&0\\0&1\\0&0\\0&1\end{pmatrix},\quad
 V=\begin{pmatrix}1&0&0&0\\0&0&1&1\end{pmatrix};\quad E=UV,\quad VU=I_2.
\]

Define \(C_k=VB^kU\) for \(k\ge0\). The first eight matrices are

\[
 C_0=\begin{pmatrix}1&0\\0&1\end{pmatrix},\quad C_1=\begin{pmatrix}0&1\\1&1\end{pmatrix},\quad C_2=\begin{pmatrix}0&0\\0&1\end{pmatrix},\quad C_3=\begin{pmatrix}1&1\\1&1\end{pmatrix},
\]
\[
 C_4=\begin{pmatrix}0&1\\1&2\end{pmatrix},\quad C_5=\begin{pmatrix}1&1\\1&2\end{pmatrix},\quad C_6=\begin{pmatrix}1&2\\2&3\end{pmatrix},\quad C_7=\begin{pmatrix}1&2\\2&4\end{pmatrix}.
\]

For \(k\ge4\), \(C_k=C_{k-2}+C_{k-3}\). Hence, using its first three applicable values, \(\operatorname{tr}(C_{n-2})=P_{n-2}\) for every \(n\ge3\). Likewise \(\operatorname{tr}(B^n)=R_n\). Direct checks of the three recurrence seeds \(n=8,9,10\) establish

\[
 \operatorname{tr}(B^n)>\operatorname{tr}(C_{n-2})>
 \operatorname{tr}(AB^{n-1})\qquad(n\ge8);
\]

the common positive recurrence propagates both strict inequalities. Moreover \(\operatorname{tr}(C_{m-2})\) is nondecreasing for \(m\ge3\) and is strictly below \(\operatorname{tr}(C_{n-2})\) whenever \(3\le m<n\) and \(n\ge8\).

**Merging separated zero runs.** Consider a word containing at least one output \(00\) and no isolated output zeros. Write its \(r\) maximal cyclic zero-runs as \(0^{h_1},\ldots,0^{h_r}\) (each \(h_i\ge2\)); let the intervening one-run lengths be \(k_1,\ldots,k_r\) (each \(k_i\ge1\)). Since \(A^{h_i}=E=UV\), cyclic trace invariance gives

\[
 d_n(y)=\operatorname{tr}(C_{k_1}\cdots C_{k_r}),\quad n'=\sum_{i=1}^r(k_i+2)\le n.
\]

For all positive integers \(a,b\), apart from \((a,b)=(1,1)\), the matrix

\[
 D(a,b)=C_{a+b+2}-C_aC_b
\]

is entrywise nonnegative and has strictly positive trace. This is a finite-base-plus-recurrence lemma: direct integer multiplication checks the \(35\) base pairs \(1\le a,b\le6\), excluding \((1,1)\). For \(a\ge7\), \(D(a,b)=D(a-2,b)+D(a-3,b)\); for \(b\ge7\) the analogous identity holds. Since the smaller first indices are at least four in the first recurrence step, induction never invokes the exceptional pair. A second direct identity is \(C_7-C_1^3=\begin{pmatrix}0&0\\0&1\end{pmatrix}\).

Use these entrywise inequalities inside any nonnegative product to merge neighboring factors \(C_aC_b\) into \(C_{a+b+2}\). For an all-\(C_1\) product of at least three factors, first merge a triple to \(C_7\); thereafter use pair merges. This ends in one factor \(C_{n'-2}\). At the final merge the trace inequality is strict, except for the sole exceptional two-factor product \(C_1^2\), whose trace is \(3\). In that exceptional case \(n'=6\) and \(3<P_{n-2}\) for \(n\ge8\). Thus all words with two or more zero-runs have strictly fewer than \(P_{n-2}\) predecessors. For one zero-run, equality requires its length to be exactly two: if it is longer, then \(n'<n\) and strict Padovan growth excludes equality. The remaining one-run is of length \(n-2\), so \(00 1^{n-2}\) achieves \(P_{n-2}\).

**Isolated output zeros.** If a non-all-one output has no \(00\), repeatedly replacing \(101\) by \(111\) until only a single zero remains gives \(d_n(y)\le\operatorname{tr}(AB^{n-1})<P_{n-2}\). The all-zero output gives \(\operatorname{tr}(A^n)=2<P_{n-2}\).

If the output contains \(00\), replace all its isolated zero bits by ones. The replacement is nondecreasing, so the resulting word is bounded by the preceding zero-run argument. To exclude any *new* equality case from replacement, suppose the final replacement leaves \(00 1^{n-2}\). Just before that last replacement the cyclic word has form \(00 1^a0 1^b\) with \(a,b\ge1\) and \(a+b=n-3\ge5\). The increase in its preimage count is exactly

\[
 g(a,b)=\operatorname{tr}(EB^{a+b+1})-\operatorname{tr}(EB^aAB^b)>0.
\]

To verify the strict sign for all \(a,b\ge1\) with \(a+b\ge5\), check the finitely many bases \(1\le a,b\le6\), \(a+b\ge5\), by exact integer multiplication; when \(a\ge7\), \(g(a,b)=g(a-2,b)+g(a-3,b)\), and similarly for \(b\ge7\). All recursively smaller indices remain in the asserted domain. Therefore isolated zeros cannot generate additional equalities.

The all-one output has \(d_n(1^n)=\operatorname{tr}(B^n)=R_n\), strictly greater than every other fiber. This completes the proof and equality classification.

## Verification
Run `python3 verify.py` with the Python standard library. The checker verifies the exact matrix identities and inequality bases, the finite sequence comparisons propagating by recurrence, and direct independent simulation of all cyclic input-output fibers for each length from eight through sixteen. The exhaustive simulation is a cross-check, **not** the proof for unbounded ring length. Successful output is `VERIFY_OK`.

## Relationship to prior work
Jen (1989) gives explicit **finite-word preimage enumeration** for Rule 54 on noncyclic strings and a finite-complement-language result; see its Proposition 2. Those results supply essential preimage-count background but, with different boundary conditions, do not themselves state this cyclic global maximum/runner-up ranking. Martínez, Adamatzky and McIntosh (2014) analyze Rule 54 via de Bruijn diagrams, gliders and dynamics, without this one-step cyclic fiber extremum. The transfer-matrix representation is standard; the contribution is the sharp all-length inequality and complete equality classification. Separate finite-ring image-set counts and results for Rule 18 address different invariants or local rules. See the accompanying originality assessment for residual historical-priority risk.

## Limitations
One synchronous Rule-54 step only, binary alphabet, indexed cyclic boundary, and \(n\ge8\). The theorem says nothing about open-boundary words, multistep preimages, decoding schemes, or complexity of general Rule-54 prediction. Historical originality has not been independently certified.

## References
1. E. Jen, *Enumeration of Preimages in Cellular Automata*, Complex Systems **3** (1989), 421–456. https://content.wolfram.com/sites/13/2018/02/03-5-2.pdf .
2. G. J. Martínez, A. Adamatzky and H. V. McIntosh, *Complete Characterization of Structure of Rule 54*, first public arXiv submission 2014-10-12, https://arxiv.org/abs/1410.3096 .
3. S. Wolfram, *Statistical Mechanics of Cellular Automata*, Reviews of Modern Physics **55** (1983), 601–644; Rule 54 background.

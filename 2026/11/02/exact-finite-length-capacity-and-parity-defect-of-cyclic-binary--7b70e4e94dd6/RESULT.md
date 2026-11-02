# Exact finite-length capacity and parity defect of cyclic binary transverse reads

## Finding

For each integer \(m\ge1\), let \(\mathcal X_m=\{0,1\}^{2m}\), with indices taken modulo \(2m\). Define the **cyclic \((3,2)\) transverse-read map** \(\Phi_m:\mathcal X_m\to\{0,1,2,3\}^m\) by
\[
\Phi_m(x)_i=x_{2i}+x_{2i+1}+x_{2i+2},\qquad 0\le i<m,
\]
where the sum is an ordinary integer sum and positions are counted with multiplicity. The indexed outputs are not identified under rotation or reversal. Then the exact size of its image, equivalently the maximum cardinality of a zero-error source code for this deterministic read map, is
\[
\boxed{N_m=|\Phi_m(\mathcal X_m)|=(2+\sqrt2)^m+(2-\sqrt2)^m-1-(-1)^m.}
\]
The parity correction is exact: the labeled-graph closed-walk trace overcounts the image by two for even \(m\) and by zero for odd \(m\). The only overcounted read vectors are the two alternating vectors in \(\{1,2\}^m\) when \(m\) is even. Consequently, the finite-block zero-error information is \(\log_2 N_m\) bits, and the limiting information rate per source bit is \(\frac12\log_2(2+\sqrt2)\). The latter asymptotic rate was previously obtained for the related noncyclic channel; the exact cyclic formula and its parity correction are the claim here.

## Assumptions and scope

The source alphabet is binary, the read length is exactly three symbols, the stride is two symbols, and every read wraps around the same length-\(2m\) cycle. The read vector has \(m\) ordered coordinates. The case \(m=1\) is included: the first and third terms refer to the same indexed bit and are summed twice. No noise, symbol deletions, unknown alignment, quotient by rotation, or probabilistic channel convention is assumed. A zero-error code is any subset of the source on which \(\Phi_m\) is injective; choosing one preimage of every attainable output proves its optimal size is \(N_m\).

For convenience write \(a_i=x_{2i}\) and \(b_i=x_{2i+1}\), for \(i\) modulo \(m\). The observation equation becomes \(y_i=a_i+a_{i+1}+b_i\). In particular, a read vector is attainable if and only if there is a closed binary-state path \((a_0,\ldots,a_{m-1},a_m=a_0)\) in which \(y_i-a_i-a_{i+1}\in\{0,1\}\) for each \(i\).

## Proof

**1. Transition matrices and subset construction.** From a binary state \(a_i\) to the next binary state \(a_{i+1}\), a labeled edge of weight \(j\in\{0,1,2,3\}\) is permitted precisely when \(j-a_i-a_{i+1}\) is a bit. With rows and columns in order \((0,1)\), the four Boolean adjacency matrices are
\[
A_0=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
A_1=\begin{pmatrix}1&1\\1&0\end{pmatrix},\quad
A_2=\begin{pmatrix}0&1\\1&1\end{pmatrix},\quad
A_3=\begin{pmatrix}0&0\\0&1\end{pmatrix}.
\]
Determinizing the nonempty subsets of binary states gives three states \(*=\{0,1\}\), \(0=\{0\}\), and \(1=\{1\}\). The transitions under symbols \(0,1,2,3\) are, respectively,

| Current state | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- | --- |
| \(*\) | \(0\) | \(*\) | \(*\) | \(1\) |
| \(0\) | \(0\) | \(*\) | \(1\) | dead |
| \(1\) | dead | \(0\) | \(*\) | \(1\) |

Thus the adjacency-count matrix of nondead transitions, with states ordered \((*,0,1)\), is
\[
T=\begin{pmatrix}2&1&1\\1&1&1\\1&1&1\end{pmatrix}.
\]
Every transition has a unique label for a given initial and final subset state, except the two distinct labeled loops at \(*\), which are counted separately by the entry 2. Therefore \(\operatorname{tr}(T^m)\) counts labeled closed state paths of marked length \(m\), with each specified read word counted once for every possible closed subset-state path.

**2. Every closed subset-state word is a genuine cyclic read vector.** Suppose a labeled closed subset path includes at least one symbol \(0\) or \(3\). A \(0\)-transition forces the next subset state to the singleton \(\{0\}\), while a \(3\)-transition forces it to \(\{1\}\). Cutting the closed path immediately after this forced transition starts and ends one full period at the same singleton. Since the subset transition of a nonempty set records all reachable binary states, the singleton-to-itself relation yields a genuine closed binary-state path following the same labels. The intermediate bits \(b_i=y_i-a_i-a_{i+1}\) then lie in \(\{0,1\}\); hence a binary source exists.

For words without \(0\) or \(3\), all labels belong to \(\{1,2\}\). If \(m\) is even, alternate binary states \(a_i=0,1,0,1,\ldots\); any off-diagonal pair allows either label \(1\) or label \(2\), by choosing \(b_i=0\) or \(1\). If \(m\) is odd, choose one edge whose label is \(1\) (if available) and assign its two endpoint states \(0,0\), or otherwise choose an edge labeled \(2\) and assign \(1,1\). Alternating across the remaining \(m-1\) edges closes consistently. This construction includes \(m=1\). Therefore every word in \(\{1,2\}^m\) is attainable. In particular every closed labeled subset-state path represents a genuine read vector.

Conversely, a genuine binary source provides a labeled cycle of binary states. If it contains a read \(0\) or \(3\), cutting after that read and propagating its forced singleton set around the full period constructs a closed deterministic subset path. Otherwise the always-present \(*\)-loops labeled \(1\) and \(2\) give a closed subset path. Thus cyclic read vectors are **exactly** the labels of closed subset-state paths.

**3. Exact multiplicities of labeled closed paths.** A label \(0\) or \(3\) synchronizes every subset path to the same singleton at its following state. Once a single state is forced, determinism uniquely determines all other states. Hence a read vector containing \(0\) or \(3\) has exactly one closed subset-state path.

For a label word entirely in \(\{1,2\}^m\), the constant subset-state path at \(*\) always exists. Any distinct closed subset path must avoid \(*\) throughout, because \(*\) cannot be left on labels \(1\) or \(2\). Within singleton states and under these two labels, the only transitions staying singleton are \(0\xrightarrow{2}1\) and \(1\xrightarrow{1}0\). Therefore an extra closed path is possible only when \(m\) is even and the read word alternates \(1,2\), in either phase. Both phase words do have exactly one such extra singleton path, while all other words have exactly one path. Consequently,
\[
|\Phi_m(\mathcal X_m)|=\operatorname{tr}(T^m)-2\mathbf1_{\{2\mid m\}}.
\]
There is no exceptional word when \(m\) is odd.

**4. Evaluate the trace.** Direct calculation gives
\[
\det(tI-T)=t(t^2-4t+2),
\]
so the eigenvalues are \(0\), \(2+\sqrt2\), and \(2-\sqrt2\). For every \(m\ge1\), \(\operatorname{tr}(T^m)=(2+\sqrt2)^m+(2-\sqrt2)^m\). Since \(2\mathbf1_{\{2\mid m\}}=1+(-1)^m\), substitution proves the asserted exact capacity formula. The positive spectral radius \(2+\sqrt2\) and the bounded parity adjustment yield the rate.

## Verification

Run `python3 verify.py` from the directory containing this file and the standalone verification script. The script constructs outputs directly from all \(4^m\) sources for \(1\le m\le10\), independently counts deterministic closed subset paths for each realized output, and compares their multiplicities to the three-state matrix trace and integer recurrence. It also checks the formula against matrix powers for all \(1\le m\le200\). It prints `VERIFY_OK` on success. The exact verified counts for \(m=1,2,3,4,5,6,7,8,9,10\) are \(4,10,40,134,464,1582,5408,18462,63040,215230\), respectively. These finite checks support, but do not substitute for, the preceding proof valid for all \(m\).

## Relationship to prior work

Chee, Vardy, Vu and Yaakobi (2021) introduced transverse-read codes and analyzed noncyclic sliding-weight read vectors. Their expanded journal treatment (2023) explicitly remarks that a cyclic version is possible but confines its results to the noncyclic version. It displays the same deterministic three-state graph (up to state permutation) and obtains the asymptotic \((3,2)\)-read rate from its Perron eigenvalue. The present claim does **not** count the graph or the asymptotic rate as new: it identifies the exact number of distinct **cyclic** marked output vectors, where the closed-path trace is not automatically the image cardinality, and proves the alternating parity correction.

Yerushalmi, Etzion and Yaakobi (2024) give asymptotic capacity results for the broader noncyclic weighted-read model; their general formula specializes to the same asymptotic rate. It does not, in the inspected material, determine the finite-period image formula above. The general theory of Artin–Mazur zeta functions for sofic shifts (as discussed by Manada and Kashyap, 2013, with reference to the classical Manning–Bowen inclusion–exclusion calculation) provides a method to count periodic output sequences from presentations, but the inspected text does not evaluate this specific read channel or identify its two alternating overcounts. The older literature on cyclic symbol-pair channels observes richer ordered symbol blocks rather than these scalar overlapping sums. These comparisons distinguish the explicit finite-period claim from previously known spectral ingredients and general algorithms.

## Limitations

Only noiseless binary length-three, stride-two **indexed cyclic** observations are covered; neither arbitrary window lengths nor other alphabets, irregular sampling, circular-output equivalence, or error correction are classified. The method relies on a particularly small deterministic presentation and a complete synchronization/multiplicity analysis; the eigenvalue computation alone would not establish the formula. Published results using equivalent symbolic-dynamics terminology may remain unindexed, and independent scientific evaluation has not been performed. No assertion of originality of the Perron eigenvalue or the asymptotic rate is made.

## References

1. Y. M. Chee, A. Vardy, V. K. Vu, and E. Yaakobi, “Coding for Transverse-Reads in Domain Wall Memories,” *Proceedings of IEEE ISIT*, 2021, pp. 2924–2929. DOI: 10.1109/ISIT45174.2021.9518271. Author-accessible full text: https://yaakobi.net.technion.ac.il/files/2022/08/124_Trans_Reads_ISIT21.pdf
2. Y. M. Chee, A. Vardy, V. K. Vu, and E. Yaakobi, “Transverse-Read-Codes for Domain Wall Memories,” *IEEE Journal on Selected Areas in Information Theory* **4** (2023), pp. 784–793. DOI: 10.1109/JSAIT.2023.3334303. Author-accessible full text: https://ymchee66.github.io/home/PDF/transverse-readj.pdf
3. O. Yerushalmi, T. Etzion, and E. Yaakobi, “The Capacity of the Weighted Read Channel,” arXiv:2401.15368 (first public January 27, 2024). https://arxiv.org/abs/2401.15368
4. A. Manada and N. Kashyap, “On the Zeta Function of a Periodic-Finite-Type Shift,” *IEICE Transactions on Fundamentals* E96-A (2013), pp. 1024–1031. DOI: 10.1587/transfun.E96.A.1024. Author-accessible full text: https://ece.iisc.ac.in/~nkashyap/Papers/pft_zeta.pdf

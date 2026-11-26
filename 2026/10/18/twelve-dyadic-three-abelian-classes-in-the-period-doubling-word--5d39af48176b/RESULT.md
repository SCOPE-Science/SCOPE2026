# Even-length three-Abelian equivalence in the period-doubling word

Let \(p\) be the fixed point starting in \(0\) of \(0\mapsto01,\ 1\mapsto00\). Two binary words are *three-Abelian equivalent* when all contiguous factors of lengths one, two and three have the same multiplicities in them. Write \(|u|_w\) for the number of occurrences of \(w\) in \(u\), including overlaps.

**Theorem.** At every even length \(n\ge4\), two length-\(n\) factors of \(p\) are three-Abelian equivalent if and only if they have equal numbers of ones and equal length-two prefixes and suffixes (with the ends ordered). In particular, to count three-Abelian classes at an even length it suffices to enumerate feasible combinations of one-count and boundary blocks, without maintaining any interior length-three counts.

**Proof.** With zero-based indexing, \(p_{2t}=0\) and \(p_{2t+1}=1-p_t\). Thus all ones are at odd positions. There are no adjacent ones, and a run of four zeros would require adjacent ones at the two parent positions of its odd-indexed letters. Consequently the internal gaps between consecutive ones contain one or three zeros.

Fix a length-\(n\) factor \(u\), with \(K\) ones and length-two boundary blocks \(a,b\) (prefix, suffix). It contains a one. Let \(L,R\) be its initial and terminal zero-run lengths. At an even start the leading run has odd length \(L=1+2\mathbf1_{a=00}\), and the trailing run has even length \(R=2\mathbf1_{b=00}\). At an odd start the parities reverse, giving \(L=2\mathbf1_{a=00}\) and \(R=1+2\mathbf1_{b=00}\). In both cases
\[
L+R=1+2\mathbf1_{a=00}+2\mathbf1_{b=00}.
\]
If \(A,B\) are the numbers of one-zero and three-zero internal gaps, then \(A+B=K-1\) and \(n=K+L+R+A+3B\). In particular
\[
|u|_{101}=A=2K-1-n/2+\mathbf1_{a=00}+\mathbf1_{b=00}.
\]
For the other counts write \(N_{xy}=|u|_{xy}\), \(C_{xyz}=|u|_{xyz}\), \(s=\mathbf1_{u_0=1}\) and \(t=\mathbf1_{u_{n-1}=1}\). Because there is no \(11\),
\[
\begin{aligned}
N_{01}&=K-s, &N_{10}&=K-t, &N_{00}&=n-1-N_{01}-N_{10},\\
C_{010}&=K-s-t,\\
C_{001}&=N_{01}-C_{101}-\mathbf1_{a=01},\\
C_{100}&=N_{10}-C_{101}-\mathbf1_{b=10},\\
C_{000}&=N_{00}-C_{001}-\mathbf1_{b=00}.
\end{aligned}
\]
Here \(N_{01}\) and \(N_{10}\) count the incoming and outgoing transitions of ones; the last three identities extend pairs by one letter on the relevant side unless that pair is at the boundary. This is the full list of possible triples. Conversely, for each length-two word \(v\), subtracting \(\sum_{c\in\{0,1\}}|u|_{vc}\) from \(|u|_v\) gives \(\mathbf1_{b=v}\); subtracting \(\sum_{c\in\{0,1\}}|u|_{cv}\) instead gives \(\mathbf1_{a=v}\). The one-letter counts give \(K\). This proves both directions.

**Scope and reproducibility.** The argument uses the opposite parities of the two endpoints at even length. It does not assert this criterion at odd lengths or in arbitrary binary words. `python3 verify_even.py` provides an exact finite check at 65 even lengths: it constructs the complete factor language at each tested length, not a prefix sample. A window of length \(n\le2^j\) lies in the concatenated level-\(j\) images of a parent pair, and the only parent pairs are \(00,01,10\), all occurring. The proof above establishes the unbounded statement.

**Prior work.** The definition and general endpoint identities are consistent with Karhumäki–Saarela–Zamboni ([arXiv:1301.5104](https://arxiv.org/abs/1301.5104)). Parreau–Rigo–Rowland–Vandomme ([arXiv:1405.3532](https://arxiv.org/abs/1405.3532), §5) study two-Abelian complexity of this word. *Dyadic higher-Abelian profiles and an exact collision law for period-doubling factors* classifies the dyadic three-Abelian profiles using circular cuts of substitution blocks; its dyadic result is not claimed here. The statement here is the reconstruction criterion for all even lengths, including the nondyadic lengths, which uses the odd-position and gap restrictions rather than rotation of a common circular word.

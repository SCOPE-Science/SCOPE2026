# Unconditional polynomial sparsity of \(M\)-unambiguous words
## Finding
Fix an ordered alphabet
\[
\Sigma=\{a_1<a_2<\cdots<a_s\}
\]
with \(s\ge2\). Let \(U_\Sigma(n)\) denote the number of \(M\)-unambiguous words over \(\Sigma\) whose length is at most \(n\). Then, for every integer \(n\ge0\),
\[
U_\Sigma(n)\le
\prod_{\ell=1}^{s}
\left(\binom{n}{\ell}+1\right)^{s-\ell+1}.
\]
In particular,
\[
U_\Sigma(n)=O_s\!\left(n^{\binom{s+2}{3}}\right),
\]
and therefore
\[
\frac{U_\Sigma(n)}
{\sum_{m=0}^{n}s^m}
=
O_s\!\left(n^{\binom{s+2}{3}}s^{-n}\right)
\longrightarrow0.
\]

This proves, without Şerbănuţă's conjecture, the density-zero conclusion that Teh explicitly left open in 2020. The statement is stronger than density zero: for every fixed alphabet, the number of \(M\)-unambiguous words up to length \(n\) is polynomial in \(n\).

## Assumptions and scope
For the fixed order \(a_1<\cdots<a_s\), the Parikh matrix \(\Psi_\Sigma(w)\) has unit diagonal and, for \(1\le i<j\le s+1\), its \((i,j)\)-entry is the number of scattered occurrences of
\[
a_i a_{i+1}\cdots a_{j-1}
\]
in \(w\). Two words are \(M\)-equivalent when their Parikh matrices agree. A word is \(M\)-unambiguous when it is the only word in its \(M\)-equivalence class.

The alphabet size \(s\) is fixed while \(n\) grows. The assumption \(s\ge2\) is necessary for the stated density conclusion: for a one-letter alphabet the Parikh matrix determines the word and the density is one.

No assumption is made about prints, ME-equivalence, strong \(M\)-equivalence, or Şerbănuţă's conjecture.

## Proof
For each length \(\ell\in\{1,\ldots,s\}\), exactly \(s-\ell+1\) nonconstant entries of a Parikh matrix count scattered occurrences of a consecutive alphabet block of length \(\ell\):
\[
a_i a_{i+1}\cdots a_{i+\ell-1},
\qquad
1\le i\le s-\ell+1.
\]

If \(|w|\le n\), then every such scattered-subword count is an integer between \(0\) and \(\binom{n}{\ell}\). Indeed, an occurrence chooses \(\ell\) increasing positions of \(w\), and there are at most \(\binom{|w|}{\ell}\le\binom{n}{\ell}\) such choices. Thus the number of Parikh matrices that can occur among words of length at most \(n\) is at most
\[
P_s(n)=
\prod_{\ell=1}^{s}
\left(\binom{n}{\ell}+1\right)^{s-\ell+1}.
\]
This product deliberately ignores dependencies among matrix entries, so it is an upper bound without any realizability assumption.

Distinct \(M\)-unambiguous words have distinct Parikh matrices. Otherwise two distinct words with the same matrix would be \(M\)-equivalent, contradicting the unambiguity of each. Consequently
\[
U_\Sigma(n)\le P_s(n).
\]

For fixed \(s\), each factor \(\binom{n}{\ell}+1\) is \(O_s(n^\ell)\), and hence
\[
P_s(n)
=
O_s\!\left(
n^{\sum_{\ell=1}^{s}\ell(s-\ell+1)}
\right).
\]
The exponent simplifies to
\[
\sum_{\ell=1}^{s}\ell(s-\ell+1)
=
\frac{s(s+1)(s+2)}6
=
\binom{s+2}{3}.
\]
Finally,
\[
\sum_{m=0}^{n}s^m=\frac{s^{n+1}-1}{s-1}
\]
for \(s\ge2\), so division by the total number of words of length at most \(n\) gives
\[
\frac{U_\Sigma(n)}{\sum_{m=0}^{n}s^m}
=
O_s\!\left(n^{\binom{s+2}{3}}s^{-n}\right)
\to0.
\]
This is the desired unconditional density-zero conclusion.

## Verification
The proof is symbolic and requires no exhaustive search. The accompanying `verify.py` is a finite consistency check, not a substitute for the argument.

The verifier directly computes all Parikh-matrix variable entries as scattered-subword counts for every binary word of length at most \(9\) and every ternary word of length at most \(7\). For every prefix length it groups words by their exact Parikh signature, counts singleton fibers, checks the singleton count against the matrix-count bound, and checks every entry against its binomial cap. As an independent sanity check on the implementation, the exact binary length-\(m\) singleton counts agree with the published formula \(6m-10\) for \(4\le m\le9\). It also verifies
\[
\sum_{\ell=1}^{s}\ell(s-\ell+1)=\binom{s+2}{3}
\]
for \(2\le s\le50\).

These finite checks test the encoding and boundary cases. The all-\(n\), all-fixed-\(s\) result follows from the counting proof above.

## Relationship to prior work
Teh's 2020 paper states the standard Parikh-matrix entry formula and defines \(M\)-unambiguity. Its Theorem 3.1 proves density zero only under Şerbănuţă's conjecture, and the paper then explicitly says that obtaining the same conclusion without that conjecture is left open. The present counting argument removes that hypothesis and gives a quantitative polynomial upper bound.

The later 2023 work of Hahn, Cheon, and Han gives a complete characterization of \(M\)-equivalence and \(M\)-unambiguity for the ternary alphabet, including a regular-language description. Its inspected full text states that the general-alphabet characterization remains elusive and does not state a general density theorem or the matrix-range counting bound used here. The 2025/2026 journal expansion has the same ternary scope in its abstract.

The result here does not characterize which matrices have singleton fibers. Instead, it observes that for fixed alphabet size the entire possible Parikh-matrix range up to length \(n\) is polynomially bounded, which already suffices for the global sparsity question.

## Limitations
The exponent \(\binom{s+2}{3}\) is only an upper-bound exponent obtained by treating matrix entries independently; no claim of sharpness is made. Dependencies among Parikh-matrix entries may substantially improve it.

The result counts \(M\)-unambiguous words globally and does not solve the much harder structural problem of characterizing them for alphabets of size at least four. Later ternary classifications therefore address a different, finer question.

Searches did not reveal an earlier publication of this counting observation, but an elementary argument of this kind could appear in an unindexed note, thesis, or brief remark. That residual originality risk remains.

## References
1. W. C. Teh, “On M-unambiguity of Parikh matrices,” Indonesian Journal of Combinatorics 4 (2020), 1–9, DOI 10.19184/ijc.2020.4.1.1.
2. J. Hahn, H. Cheon, and Y.-S. Han, “M-equivalence of Parikh Matrix over a Ternary Alphabet,” in Implementation and Application of Automata, LNCS 14151 (2023), 141–152, DOI 10.1007/978-3-031-40247-0_10.
3. J. Hahn, H. Cheon, and Y.-S. Han, “Characterizations of M-Equivalence and Weak M-Relation,” International Journal of Foundations of Computer Science 37 (2026), 73–92, DOI 10.1142/S0129054125410047.

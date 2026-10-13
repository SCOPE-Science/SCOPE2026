# Exact optimum for binary \(1,7\)-overlap-free codes

## Finding

Let \(C(n,7)\) be the largest cardinality of a set \(\mathcal C\subseteq\{0,1\}^{n}\) such that no nonempty prefix of a word of \(\mathcal C\) of length at most \(7\) equals the suffix of the same length of any (possibly the same) word of \(\mathcal C\). Then, for **every integer \(n\ge14\)**,
\[
\boxed{C(n,7)=744\,2^{n-14}.}
\]
Thus the previously published lower bound \(744\,2^{n-14}\) is optimal, including among codes not constrained to the published construction.

## Assumptions and scope

Words are binary; comparison is between prefixes and suffixes across *ordered* pairs of codewords, including self-overlaps. Only overlap lengths \(1,2,\ldots,7\) are forbidden. The statement is for fixed word lengths \(n\ge14\); it does not treat shorter words, larger overlap cutoffs, variable-length codes, or additional decoding constraints.

## Proof

**Step 1 (boundary reduction).** For a nonempty admissible code, let \(P\) and \(S\) be its sets of seven-bit prefixes and seven-bit suffixes. The forbidden length-one overlap forces every word to start with one binary symbol and end with the other. By exchanging the symbols, assume that every element of \(P\) begins with \(0\) and every element of \(S\) ends with \(1\). There are precisely \(64\) possible prefixes and \(64\) possible suffixes after this normalization.

Write these possible prefixes as the seven-bit encodings \(p_i\) of \(i\in\{0,\ldots,63\}\), and suffixes as the encodings \(s_j=2j+1\) for \(j\in\{0,\ldots,63\}\). Define the binary compatibility relation
\[
R(i,j)\iff \forall t\in\{1,\ldots,7\}:\ \operatorname{pref}_t(p_i)\ne\operatorname{suff}_t(s_j).
\]
Any valid code must satisfy \(R(i,j)\) for every \(i\in P\) and \(j\in S\). Once these boundary pairs are compatible, all \(2^{n-14}\) possible middle blocks may be used without introducing a forbidden overlap. Consequently
\[
C(n,7)=2^{n-14}\max_{P,S\text{ compatible}} |P|\,|S|.
\]
(The general prefix/suffix reduction also appears as Theorems 7–8 of Blackburn et al.; it is not asserted here as novel.)

**Step 2 (closure reduction).** For any prefix subset \(X\), let \(N(X)\) be the suffixes compatible with every prefix in \(X\). For any suffix subset \(Y\), let \(N^*(Y)\) be the prefixes compatible with every suffix in \(Y\). Set
\[
\operatorname{cl}(X)=N^*(N(X)).
\]
These are the two antitone maps of a finite Galois connection. Directly from their definitions, \(X\subseteq\operatorname{cl}(X)\), \(N(\operatorname{cl}(X))=N(X)\), and \(\operatorname{cl}\) is monotone and idempotent. Given compatible \((P,S)\), replacing it with \((\operatorname{cl}(P),N(P))\) never decreases the size product. Therefore only closed prefix sets \(X=\operatorname{cl}(X)\) need be considered, with objective \(|X|\,|N(X)|\).

**Step 3 (exhaustive finite upper bound).** The attached `verify.py` constructs the complete \(64\)-by-\(64\) relation using all seven forbidden overlap tests, and enumerates all closed prefix subsets using the following standard, exact lectic successor. Starting from \(X=\operatorname{cl}(\varnothing)\), scan \(j=63,62,\ldots,0\). Whenever \(j\notin X\), form
\[
Y_j=\operatorname{cl}\bigl((X\cap\{0,\ldots,j-1\})\cup\{j\}\bigr).
\]
The first \(j\) satisfying \(Y_j\cap\{0,\ldots,j-1\}=X\cap\{0,\ldots,j-1\}\) gives the next closed set; if no such \(j\) exists, the enumeration ends. To see completeness, order subsets lectically by the smallest element at which they differ. In any later closed set, the least differing index must be added, and closure cannot change any earlier index; conversely the largest valid pivot in the displayed scan yields the immediate next closed set, since any earlier candidate would conflict with its already prescribed initial segment. Thus there are no skipped closed sets. The computation visits **exactly \(1,944\) closed prefix sets**, and evaluates
\[
\max_{X=\operatorname{cl}(X)} |X|\,|N(X)|=744.
\]
Every relation entry, closure, successor test, and cardinality is computed with exact integer operations. A dual enumeration from the suffix side independently gives the same \(1,944\) concept pairs and maximum. As checks of the enumeration method, it gives the established products \(64\) and \(216\) at cutoffs \(5\) and \(6\); for cutoff \(5\), a separate direct enumeration of all \(2^{16}\) prefix subsets gives \(64\).

**Step 4 (attainment).** Choose the \(24\) prefixes \(p_0,\ldots,p_{23}\). Direct overlap comparison yields \(|N(P)|=31\). Include every concatenation of a chosen prefix, any \((n-14)\)-bit middle block, and one of the \(31\) compatible suffixes. This has \(24\cdot31\cdot2^{n-14}=744\cdot2^{n-14}\) codewords, with all prescribed overlaps excluded. The upper and lower bounds coincide. \(\square\)

## Verification

Run `python3 verify.py` with the Python standard library. The exact outputs include `k=7`, `concepts=1944`, `max_prod=744`, `witness_P=24`, `witness_S=31`, and `VERIFY_OK`. The code rebuilds the relation from the word definition and has no stored optimality table or external dependencies. Finite verification here covers the complete 64-by-64 boundary search; the extension to **every \(n\ge14\)** is the proved boundary reduction, not extrapolation from finitely many values of \(n\).

## Relationship to prior work

Blackburn, Nasr Esfahani, Kreher, and Stinson introduced the restricted-overlap coding problem and proved the graph reduction. They obtained exact optima through cutoff \(6\), and explicitly constructed the \(24\)-by-\(31\) solution at cutoff \(7\), giving only the lower bound \(744\cdot2^{n-14}\), while their general upper bound remains strictly larger. The contribution here is an exact exhaustive **upper bound at cutoff \(7\)** establishing that their previously known construction is globally optimal. General results on non-overlapping codes, where *all* proper overlap lengths are forbidden, are not an equivalent evaluation of this fixed restricted-overlap case.

## Limitations

The proof uses a complete finite exact enumeration for the fixed cutoff \(7\). It supplies neither a formula for larger cutoffs nor a mathematical characterization of all extremal codes. An equivalent independently obtained enumeration not discoverable in the inspected literature cannot be excluded. The self-review does not constitute independent validation.

## References

1. S. R. Blackburn, N. Nasr Esfahani, D. L. Kreher, and D. R. Stinson, *Constructions and bounds for codes with restricted overlaps*, arXiv:2211.10309 (first public 2022-11-18), Sections IV–V and VII; https://arxiv.org/html/2211.10309v4 .
2. MSC2020 classification \(94\mathrm{A}45\), prefix, length-variable and comma-free codes; https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=94A20 .

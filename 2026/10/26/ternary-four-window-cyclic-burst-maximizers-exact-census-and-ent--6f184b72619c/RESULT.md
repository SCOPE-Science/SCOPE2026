# Ternary four-window cyclic-burst maximizers: exact census and entropy

## Finding
Let \(\Sigma=\{0,1,2\}\). For a word \(x\in\Sigma^n\), \(n\ge4\), let \(B_4(x)\) contain \(x\) and all *distinct* words obtained by rotating one non-wrapping consecutive four-letter factor left by one, two, or three positions. Then
\[
\max_{x\in\Sigma^n}|B_4(x)|=3n-8\qquad(n\ge4).
\]
Write \(F_n=|\{x\in\Sigma^n:|B_4(x)|=3n-8\}|\). The complete extremizer census, for every length, is \(F_4=72\) and
\[
\boxed{\displaystyle
\sum_{n\ge5}F_n z^{n-5}=
\frac{6(21+20z+17z^2-7z^3-63z^4-32z^5-26z^6+20z^7+28z^8-48z^9)}
{1-z-z^2-2z^3-2z^4+4z^5+2z^6+3z^7-z^8-4z^9+4z^{10}}.}
\]
In particular, \(F_5,F_6,\ldots,F_{14}\) equal
\[
126,246,474,930,1770,3444,6630,12828,24774,47850.
\]
The extremal words have a primitive finite-state presentation on exactly 21 normalized five-letter states and 41 allowed transitions. They have exponential growth constant
\[
\rho=1.931675158058\ldots,
\qquad F_n\sim c\rho^n\text{ for some }c>0.
\]
Here \(\rho\) is the Perron eigenvalue of the explicitly given transition matrix below, equivalently the largest-modulus root of
\[
t^{10}-t^9-t^8-2t^7-2t^6+4t^5+2t^4+3t^3-t^2-4t+4.
\]
Thus the fraction \(F_n/3^n\) of input words attaining maximal ambiguity decays exponentially. The same sharp maximum \(3n-8\) holds for every alphabet with at least three symbols, since the witness below uses only three.

## Assumptions and scope
The error changes exactly one *window* of four consecutive positions without wrapping at the ends; the identity operation is included. Repeated output words are counted only once. All statements about the census, rational generating function, transition graph and growth constant concern the labeled **three-symbol** alphabet and all integer lengths \(n\ge4\). The result does not concern arbitrary permutations within a four-window, nor windows of lengths less than four.

## Proof
**Universal bound and an infinite attaining family.** There are \(n-3\) four-windows and at most three nonidentity cyclic shifts per window, so \(|B_4(x)|\le1+3(n-3)=3n-8\). Every prefix of length \(n\ge4\) of the periodic word \((000121)^\infty\) attains equality. Its initial four- and five-letter prefixes contribute respectively three and six new nonidentity outputs. Subsequently the new-window increment is three for each of the six consecutive six-letter factors of the period: `000121`, `001210`, `012100`, `121000`, `210001`, `100012`. Direct comparison of their rotations against the two preceding overlapping windows verifies this assertion. The finite local calculation is reproduced by `verify.py`.

**Why six letters suffice.** Appending one symbol preserves every old output, with the same appended symbol. All newly possible outputs arise by rotating the final four-window. For a new nonidentity output to coincide with an output from an older four-window, the two windows must overlap in at least two positions: a permutation cannot change exactly one coordinate of a word. Consequently only the two immediately preceding windows can matter; windows beginning at least three positions earlier overlap in at most one coordinate. The new-window contribution therefore depends solely on the final six symbols, once the word length is at least six. This proves genuine locality for *all* lengths, not merely for those tested.

**Extremal-language automaton.** A prefix of an extremal word must itself be extremal, since each additional four-window supplies at most three new outputs. At length five there are exactly 126 extremal words, falling into 21 patterns up to global relabeling of symbols, each pattern having six labeled representatives. In a canonical pattern, rename the first distinct symbol `0`, the next new symbol `1`, and any third new symbol `2`. A transition between canonical five-letter states is allowed precisely when appending a letter contributes three new outputs in the six-letter context. The complete adjacency list (each edge has weight one) is:

```text
00012: 00121 00122
00102: 01021 01022
00112: 01120 01121 01122
00121: 01210 01211
00122: 01220 01221 01222
01002: 01120 01121 01122
01021: 01201 01202
01022: 01220 01221 01222
01102: 00121 00122
01110: 00012
01112: 00012
01120: 00121 00122
01121: 00102
01122: 00112
01201: 01201 01202
01202: 01210 01211
01210: 01021 01022
01211: 01002
01220: 01120 01121 01122
01221: 01102
01222: 01110 01112
```

The list is finite and completely reproducible: examine the \(3^5=243\) five-letter words, retain those with seven distinct outputs, canonically relabel, and test each of the three extensions against the old five-letter ball. Every five-letter state has six distinct original labelings, including those using exactly two symbols, since \((3)_2=(3)_3=6\). Canonical relabeling of the new five-letter suffix preserves the exact multiplicity of extensions. Let \(A\) denote the resulting \(21\)-by-\(21\) zero-one adjacency matrix, with rows and columns ordered as displayed, and let \({\bf1}\) be the all-ones column. For every \(n\ge5\),
\[
F_n=6\,{\bf1}^{\mathsf T}A^{n-5}{\bf1}.
\]

**Exact rational form.** Integer matrix arithmetic applied to the displayed table gives
\[
\det(I-zA)=1-z-z^2-2z^3-2z^4+4z^5+2z^6+3z^7-z^8-4z^9+4z^{10}.
\]
Moreover, putting \(Q(t)=t^{10}-t^9-t^8-2t^7-2t^6+4t^5+2t^4+3t^3-t^2-4t+4\), the *exact vector identity* \({\bf1}^{\mathsf T}Q(A)=0\) holds. Both finite identities are directly checked from the displayed graph with the integer-only standalone `verify.py`; its characteristic-polynomial computation uses Newton identities rather than floating-point eigenvalues. It follows that \(F_n\) obeys the corresponding order-ten linear recurrence for all lengths. Substitution of the first ten exactly counted values yields the stated rational generating function. This is an infinite identity justified by a finite algebraic certificate, not by extrapolation.

**Entropy.** All 21 states communicate, and the transition `01201` to itself is a self-loop. Thus \(A\) is primitive, so the Perron–Frobenius theorem gives \(F_n\sim c\rho^n\) with \(c>0\). Direct numerical root evaluation of the exact characteristic factor yields the displayed \(\rho\).

## Verification
Run `python verify.py` with the standard Python 3 library. The script reconstructs the channel's actual output sets; exhaustively checks all words of lengths four through nine; checks local increments against full prefix balls for all words of lengths seven through nine; constructs the 21-state graph from its definition; verifies every state's reachability and a self-loop; computes \(\det(I-zA)\) exactly using integer Newton identities; verifies the vector annihilator and all generating-function coefficients; and verifies the six-factor periodic construction. The shipped `verification_output.txt` ends with `VERIFY_OK`.

## Relationship to prior work
Chen and Milenkovic (arXiv:2610.15701v1, first public October 11, 2026) introduce the substring-permutation and cyclic-substring-permutation error models. Their paper explicitly treats binary inputs and studies redundancy bounds and code constructions. The present question concerns the complete *ternary equality-case language* for fixed exact four-window cyclic rotations, a different invariant that is not supplied by their bounds. Work on fixed-length burst Levenshtein balls studies deletion followed by insertion rather than a permutation of the existing four positions and therefore does not imply this equality classification.

## Limitations
Only the number of maximally ambiguous centers, not the distribution of all nonmaximum ball sizes, is determined. This is a combinatorial channel theorem, not a construction of a large error-correcting code or a decoding algorithm. The numerical growth constant is an approximation; the rational generating function, transition graph and recurrence are exact. Possible equivalent statements in unindexed or unpublished research cannot be excluded by literature searches alone.

## References
1. Yuan-Pon Chen and Olgica Milenkovic, *Correcting Burst Errors with Applications to DNA-Based Data Storage*, arXiv:2610.15701v1 (first publicly posted 2026-10-11), https://arxiv.org/html/2610.15701v1.
2. Yuanxiao Xi, Yubo Sun and Gennian Ge, *On the Fixed-Length-Burst Levenshtein Ball with Unit Radius*, arXiv:2506.07817v1 (first publicly posted 2025-06-09), https://arxiv.org/abs/2506.07817.

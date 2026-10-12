# Complete binary order-four universal partial-word enumerator

## Finding

Let a **linear binary universal partial word of order four** be a finite string over the alphabet \(\{0,1,\diamond\}\) such that each of the \(16\) binary words of length \(4\) matches exactly one consecutive window of length \(4\). A wildcard \(\diamond\) matches either binary letter; windows do not wrap around. Strings with different starting positions, reversals, or bit-complementations are counted as distinct unless literally identical.

Let \(N_{\ell,d}\) be the number of such strings with length \(\ell\) and exactly \(d\) wildcards. Their **complete bivariate enumerator** is

\[
\begin{aligned}
P(X,Y)&=\sum_{\ell,d}N_{\ell,d}X^{\ell}Y^d\\
&=X^4Y^4+4X^8Y^3+4X^{11}Y^2+16X^{11}Y^3\\
&\quad+8X^{14}Y^2+16X^{15}Y+8X^{16}Y\\
&\quad+8X^{17}Y+64X^{18}Y+256X^{19}.
\end{aligned}
\]

Consequently there are exactly \(385\) distinct strings: \(256\) contain no wildcard, one is the all-wildcard string, and exactly \(128\) are nontrivial. Under reversal and bit complementation, the \(128\) nontrivial strings form precisely \(32\) orbits, all of size \(4\). Among all strings there are \(96\) size-four orbits and one size-one orbit.

The full indexed-string list and the \(32\) lexicographically least nontrivial orbit representatives are provided as `all_words.txt` and `orbit_representatives.txt`. In these machine-readable files, `*` denotes \(\diamond\).

## Assumptions and scope

The statement concerns **linear** (not cyclic) partial words, exactly binary base alphabet, factor length exactly \(4\), and exact-once coverage by starting position. A binary factor matched by two different windows is counted twice, even when the same wildcard can be instantiated differently in the two windows. No identifications are made in the enumerator itself. Reversal and complementation are only used for the separately stated orbit count.

## Proof

Write \(U=\{0,1\}^4\). For a length-four partial pattern \(q\), let
\[C(q)=\{u\in U:\text{each specified bit of }q\text{ equals the corresponding bit of }u\}.\]
Every \(C(q)\) is nonempty and has cardinality \(2^h\), where \(h\) is the number of wildcards in \(q\).

Take any three-character initial prefix \(p\in\{0,1,\diamond\}^3\), and initialize its covered set to \(S=\varnothing\). Given the last three characters \(t\) and the set \(S\subseteq U\) already covered by prior windows, append \(a\in\{0,1,\diamond\}\). This creates exactly one new window \(q=ta\). Reject the extension if \(C(q)\cap S\ne\varnothing\); otherwise extend with state
\[(t',S')=(\operatorname{suffix}_3(ta),\ S\cup C(ta)).\]
Stop and record the string at \(S=U\). There are exactly \(27\) choices of the initial prefix, and at most \(16\) subsequent accepted extensions, because every new window covers at least one previously uncovered factor. Hence **every** valid string has length between \(4\) and \(19\).

Completeness follows inductively: any prefix of a valid universal partial word has disjoint coverage sets for its consecutive windows, since an overlap already duplicates a binary factor and can never be undone by further append operations. Therefore no prefix of a valid string is rejected. Conversely, if this recursion reaches \(S=U\), the pairwise-disjoint nonempty matched sets partition all \(16\) factors, proving exactly-once coverage. No longer valid string can follow a terminal state because any next window would overlap \(U\). A string has precisely one initial prefix and one sequence of appended characters, so it is counted exactly once. This establishes that the finite recursion is an exhaustive proof procedure, rather than a statistical sampling method.

The `enum.cpp` implementation enumerates this recursion using \(16\)-bit masks with independent four-pattern expansion; its complete terminal counts are

| String length \(\ell\) | Wildcards \(d\) | \(N_{\ell,d}\) |
| ---: | ---: | ---: |
| 4 | 4 | 1 |
| 8 | 3 | 4 |
| 11 | 2 | 4 |
| 11 | 3 | 16 |
| 14 | 2 | 8 |
| 15 | 1 | 16 |
| 16 | 1 | 8 |
| 17 | 1 | 8 |
| 18 | 1 | 64 |
| 19 | 0 | 256 |

All other pairs have coefficient zero. The recursion visits \(15{,}840\) finite search nodes, including initial prefixes. Independently, `verify.py` implements direct character matching with explicit sets rather than integer masks, generates all \(385\) strings, and checks exact-once coverage separately for **every** generated string. The two implementations yield identical terminal counts. The full list provides an additional independently inspectable finite certificate. Applying the explicit reversal/complement operations to that list verifies the \(32\) and \(96\) orbit counts. This proves the stated enumerator and orbit consequences.

## Verification

With a C++17 compiler and Python 3, run from the directory containing the supplied files:

```sh
g++ -O2 -std=c++17 enum.cpp -o enum
./enum
python3 verify.py --check all_words.txt --check-reps orbit_representatives.txt
```

The C++ program prints all ten nonzero profile entries and reports `nodes=15840 bins=10`. The Python program reports `NODES 15840 WORDS 385 ORBITS {1: 1, 4: 96}` and terminates with `VERIFY_OK`. Its verification performs a fresh factor-by-factor check of every listed string, confirms uniqueness, and checks reversal/complement closure. All \(12\) order-four example strings displayed across Tables 1–3 of Chen–Kitaev–Mütze–Sun were separately found in the computed list.

## Relationship to prior work

Chen, Kitaev, Mütze and Sun introduced and investigated universal partial words, supplied existence/nonexistence results and numerous specific binary order-four examples, and explicitly proposed complete classification questions. Those constructions and examples are not claimed as new here. The new, more specific invariant is the **complete joint length-by-wildcard enumerator for the linear binary order-four case**, including every possible length and count; a collection of examples or existence theorems does not determine these coefficients.

Goeckner and coauthors later developed nonbinary results and explicitly asked how many universal partial words exist for specified alphabet and order. This exact small-parameter classification addresses that enumerative question, with no claim to general larger-order enumeration. Previously published results on ordinary de Bruijn sequences already account for the \(256\) no-wildcard strings; this known subcase is included for completeness, not presented as a discovery.

## Limitations

The enumeration applies **only** to linear binary order-four strings. It does not enumerate cyclic universal partial words, higher factor lengths, or nonbinary alphabets. The exhaustive computational proof is finite and fully specified by the recurrence and supplied programs; no unproved statement for arbitrary order is inferred. Earlier unpublished computational lists or unindexed enumerations may contain the same specific coefficients; originality is subject to that residual bibliographic risk.

## References

1. H. Z. Q. Chen, S. Kitaev, T. Mütze and B. Y. Sun, *On universal partial words*, arXiv:1601.06456, initially public 2016-01-25; Discrete Mathematics & Theoretical Computer Science 19:1 (2017), article 16, DOI:10.23638/DMTCS-19-1-16. Original 18-page text inspected, especially Tables 1–3, Sections 1 and 6.
2. H. Z. Q. Chen, S. Kitaev, T. Mütze and B. Y. Sun, *On universal partial words*, Electronic Notes in Discrete Mathematics 61 (2017), pp. 231–237. Open author manuscript inspected in full, including the examples and research directions.
3. B. Goeckner, C. Groothuis, C. Hettle, B. Kell, P. Kirkpatrick, R. Kirsch and R. Solava, *Universal partial words over non-binary alphabets*, arXiv:1611.03928 (initially public 2016-11-12), Theoretical Computer Science 713 (2018), pp. 56–65. Sections on definitions, constructions and Question 6.5 inspected in an accessible textual rendition; complete PDF not retrieved.

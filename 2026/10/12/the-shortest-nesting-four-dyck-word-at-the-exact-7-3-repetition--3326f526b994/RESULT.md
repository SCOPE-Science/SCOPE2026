# The shortest nesting-four Dyck word at the exact \(7/3\) repetition boundary
## Finding
Let a binary Dyck word use \(0\) as a left parenthesis and \(1\) as a right parenthesis. Its nesting level is the maximum prefix balance \(|u|_0-|u|_1\). Call a word \(7/3^+\)-power-free when none of its factors has exponent strictly larger than \(7/3\).

The shortest \(7/3^+\)-power-free Dyck word of nesting level \(4\) has length
\[
24.
\]
It is unique:
\[
\mathtt{001001100100110110011011}.
\]
The word is fixed by reverse-complementation. It lies exactly on the repetition boundary: the factor \(\mathtt{1001001}\) has period \(3\) and exponent \(7/3\), while no factor has exponent greater than \(7/3\).

## Assumptions and scope
For a nonempty word \(x\), its exponent is \(|x|/\operatorname{per}(x)\), where \(\operatorname{per}(x)\) is its least positive period. The strict notation \(7/3^+\)-power-free therefore allows factors of exponent exactly \(7/3\) and forbids only factors of exponent greater than \(7/3\).

The claim concerns the first nesting level that is impossible under the non-strict \(7/3\)-power-free condition. Mol, Rampersad, and Shallit prove that every \(7/3\)-power-free binary Dyck word has nesting level at most \(3\), while \(7/3^+\)-power-free Dyck words exist at every nesting level. No assertion is made here about the shortest words at nesting levels greater than \(4\).

## Proof
The displayed word has twelve \(0\)'s and twelve \(1\)'s. Its prefix balances are nonnegative, return to \(0\), and attain \(4\), so it is a Dyck word of nesting level \(4\).

For power avoidance, every factor \(y\) and every candidate period \(p\) are checked exactly. A factor violates \(7/3^+\)-power-freeness precisely when
\[
3|y|>7p
\]
and \(p\) is a period of \(y\). No factor of the displayed word satisfies these two conditions. On the other hand, \(\mathtt{1001001}\) occurs as a factor, has length \(7\), and has period \(3\), so the maximal exponent is exactly \(7/3\).

For minimality and uniqueness, exhaust all Dyck words at every even length through \(24\). A prefix-pruned enumeration keeps exactly those prefixes that are still Dyck-compatible and have created no factor of exponent greater than \(7/3\). Because appending one symbol can create only forbidden factors ending at the new symbol, checking all new suffixes is exhaustive. The resulting numbers of \(7/3^+\)-power-free Dyck words at lengths \(2,4,\ldots,24\), split by nesting level, are recorded in `certificate.json`.

There is no nesting-level-\(4\) survivor at any even length below \(24\). At length \(24\) there are \(77\) survivors in total: \(40\) of nesting level \(2\), \(36\) of nesting level \(3\), and exactly one of nesting level \(4\), namely the displayed word. Hence the minimum length is \(24\) and the minimizer is unique.

## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier uses two exact enumeration routes. The first is the prefix-pruned construction described in the proof. The second independently generates every Dyck word of nesting level at most \(4\) with no repetition pruning, then inspects every factor and every possible period from scratch. For the level-\(4\) slice, the two routes agree at every even length from \(8\) through \(24\), while the first route reproduces the complete count table from length \(2\).

The verifier separately confirms nesting level \(4\), the exact \(7/3\)-power factor \(\mathtt{1001001}\), absence of any factor of larger exponent, uniqueness at length \(24\), and invariance under reverse-complementation.

## Relationship to prior work
Mol, Rampersad, and Shallit prove two endpoint facts. First, every binary Dyck word avoiding powers of exponent at least \(7/3\) has nesting level at most \(3\). Second, after changing to the strict condition and allowing exact \(7/3\)-powers, they construct \(7/3^+\)-power-free Dyck words of every nesting level. Their explicit even-level family is \(f(g^t(2))\), with \(g\) \(6\)-uniform and \(f\) \(38\)-uniform; the member supplied by that construction at nesting level \(4\) therefore has length \(228\).

The source does not determine the minimum length at nesting level \(4\), list the shortest witnesses, or claim uniqueness. Searches using the exact witness, “nesting level 4”, “shortest”, “minimum length”, and both \(7/3\)-power-free conventions did not locate a published statement implying the length-\(24\) classification. The earlier paper on Dyck words and abelian borders studies enumeration by abelian-border statistics rather than repetition avoidance, so it does not cover this claim.

## Limitations
This is an exact finite classification at the first newly attainable nesting level. It does not give a formula for the minimum length as a function of nesting level, nor does it improve the source's existence theorem for arbitrarily large nesting levels.

The originality search cannot exclude an unindexed computation or unpublished note. The proof is exhaustive but finite; its all-cases force comes from enumerating the complete Dyck search space through the claimed minimum, not from an asymptotic argument.

## References
1. L. Mol, N. Rampersad, and J. Shallit, “Dyck Words, Pattern Avoidance, and Automatic Sequences,” arXiv:2301.06145, first public version 2023-01-15; Communications in Mathematics 33 (2025), Paper 5, DOI 10.46298/cm.12695.
2. F. Blanchet-Sadri, K. Chen, and K. Hawes, “Dyck Words, Lattice Paths, and Abelian Borders,” arXiv:1708.06461; EPTCS 252 (2017), 56–70, DOI 10.4204/EPTCS.252.9.

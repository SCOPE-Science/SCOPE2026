# Global versus local deletion witnesses at the length-\(13\) irreducible square-free boundary
## Finding
For a ternary irreducibly square-free word \(w\), define its deletion-witness radius
\[
\rho(w)=\max_{1\le i\le |w|-2}\min\{p:\text{ deleting position }i\text{ creates a square of period }p\}.
\]
At length \(13\), exactly \(30\) labeled irreducibly square-free words occur. Their deletion-witness radii split exactly as
\[
18\text{ words with }\rho=3,\qquad 12\text{ words with }\rho=6.
\]

Up to alphabet permutations and reversal, the three length-\(13\) classes are represented by
\[
\mathtt{0102012101202},\qquad
\mathtt{0102012102010},\qquad
\mathtt{0102120102012},
\]
with orbit sizes \(12,6,12\) and radii \(3,3,6\), respectively.

Thus exactly one symmetry class has genuinely global deletion fragility. For the representative
\[
w=\mathtt{0102120102012},
\]
deleting its \(11\)th letter gives
\[
\mathtt{010212010212}=(\mathtt{010212})^2,
\]
and this twelve-letter word contains no square of period smaller than \(6\). Every word in this orbit has exactly one interior deletion with least square period \(6\). Every deletion in each of the other two classes is already witnessed by a square of period at most \(3\).

## Assumptions and scope
The alphabet is \(\{0,1,2\}\). A square is a factor \(XX\) with \(X\ne\epsilon\), and its period is \(|X|\). A word is square-free if it contains no square. It is irreducibly square-free if it is square-free, has length at least \(3\), and deleting any interior letter creates a square.

The least square period after a deletion is taken over all square factors of the resulting word, not just squares meeting the deletion site. The radius \(\rho(w)\) is then the worst such least period over all interior deletions.

Length \(13\) is singled out because Harju's exact existence theorem has \(12\) as the last excluded length: irreducibly square-free ternary words exist at lengths \(3,6,8,9,10,11\) and at every length at least \(13\).

## Proof
First enumerate all ternary square-free words of length \(13\). Prefix extension is exhaustive because square-freeness is factorial. When a letter is appended to a square-free prefix, any newly created square must be a suffix, so rejecting extensions with a square suffix is exact. This produces \(342\) square-free words.

For every such word, delete each of its \(11\) interior positions and rescan the resulting word for squares. Exactly \(30\) words have a square after every deletion, hence are irreducibly square-free.

For every accepted word and every interior deletion, enumerate all square factors of the resulting length-\(12\) word and record their least period. Taking the maximum over deletions gives \(\rho(w)\). The resulting histogram is exactly
\[
\rho=3:18,\qquad \rho=6:12.
\]
No other radius occurs.

To quotient by symmetry, apply all six permutations of the alphabet and reversal. The \(30\) words form three orbits, represented by the three words in the Finding section, of sizes \(12,6,12\). The first two representatives have radius \(3\); the third has radius \(6\).

For the third representative, deletion of the \(11\)th letter gives the full square \((\mathtt{010212})^2\). A direct scan of that result finds no square of period \(1,2,3,4,\) or \(5\). Repeating this check across its full symmetry orbit shows that every one of the \(12\) words has exactly one such period-\(6\) deletion. No word in the other two orbits has one.

## Verification
Run `python3 verify.py` beside `certificate.json`.

One enumeration engine builds only square-free prefixes using a suffix-square invariant. A second engine independently scans all \(3^{13}\) ternary words directly for square factors. The two engines must return the same \(342\) words.

The verifier then checks irreducibility by all \(11\) deletions, obtaining \(30\) words. Two differently ordered square-period scans must agree after every deletion. Finally, the verifier recomputes the radius histogram, all three symmetry orbits, their sizes, and the unique global deletion site in every radius-\(6\) word.

## Relationship to prior work
Harju introduced irreducibly square-free ternary words and proved that they exist exactly at lengths \(3,6,8,9,10,11\) and every length at least \(13\). His systematic search already reports that length \(13\) has three classes up to alphabet permutation and reversal, and gives one length-\(13\) example. That prior result therefore covers the number of symmetry classes, but it does not compare the periods of the squares created by deletion.

Przybocki later restated Harju's exact length spectrum while developing analogous results for irreducible overlap-free and cubefree words and for delicate words. The later article likewise treats existence and length classification rather than the least period of the square certifying each deletion.

The present refinement is the deletion-certificate structure inside the already known three-class boundary: two classes are locally witnessed with radius \(3\), while the third is globally witnessed with radius \(6\).

## Limitations
The radius classification is only for length \(13\). It does not assert any pattern for longer irreducibly square-free words. The source's three-class count is prior work and is used only as an external consistency anchor; the verifier independently regenerates the complete labeled layer.

Unindexed computational notes associated with the original systematic search could contain the same period profiles even though the inspected paper and later length-classification paper do not report them.

## References
1. T. Harju, “Disposability in Square-Free Words,” arXiv:1911.09973v1, first public version 2019-11-22; Theoretical Computer Science 862 (2021), 155–159, DOI 10.1016/j.tcs.2020.07.030.
2. B. Przybocki, “Lengths of Irreducible and Delicate Words,” Electronic Journal of Combinatorics 29(3) (2022), #P3.7, DOI 10.37236/10669.

# Complete abelian-complexity classification of balanced binary four-uniform substitutions

## Finding
Let \(\sigma(0)=u\) and \(\sigma(1)=v\), with \(u,v\in\{0,1\}^4\), two occurrences of each letter in both images, and first symbol of \(u\) equal to 0. Put \(x=\sigma^\omega(0)\). Let \(a_x(n)\) be the number of distinct Parikh vectors of length-\(n\) contiguous factors of \(x\), for every integer \(n\ge1\). In a row `u/v`, the first string is the image of 0, the second the image of 1.

The exact classification of the 18 substitutions is:

| Morphisms `u/v` | Exact values of \(a_x(n)\) |
|---|---|
| `0011/0011`, `0110/0110` | 1 for \(n\equiv0\pmod4\), 3 for \(n\equiv2\pmod4\), 2 for odd \(n\) |
| `0101/0101` | 1 for even \(n\), 2 for odd \(n\) |
| `0110/1100`, `0110/0011`, `0011/0110`, `0011/1001` | 2 at \(n=1\); 3 for \(n\ge2\) |
| `0110/1010`, `0110/1001`, `0110/0101`, `0101/1010`, `0101/1001`, `0101/0110`, `0101/0011`, `0011/0101` | 2 for odd \(n\), 3 for even \(n\) |
| `0101/1100`, `0011/1010` | 2 at \(n=1\); 4 for odd \(n\ge3\), 3 for even \(n\) |
| `0011/1100` | 2 at \(n=1\); 5 for \(n\equiv0\pmod4\), 3 for \(n\equiv2\pmod4\), 4 for odd \(n\ge3\) |

Moreover, for every one of the 15 morphisms with \(u\ne v\), for every \(d\ge1\) and every \((a,b)\in\{0,1\}^2\) there exists \(j\ge0\) with \(x_j=a\) and \(x_{j+d}=b\). In particular, each of the 18 complexity functions is periodic from length 2 onward, with period dividing four.

## Assumptions and scope
All words are infinite right-sided fixed points, factors are contiguous, and counts refer to ordinary integer counts of ones. In the binary case the Parikh vector is determined by the number of ones. The substitution is four-uniform and balanced, not an arbitrary Parikh-collinear substitution. Exactly three balanced four-letter binary words start in 0 (`0011`, `0101`, `0110`); the second image can be any of six balanced four-letter words.

## Proof
**1. Full separated-pair lemma.** Assume \(u\ne v\). For every \(d\ge1\) write
\[P(d)=\{(x_j,x_{j+d}):j\ge0\}.\]
The literal finite certificate in `verify.py` checks, for all 15 unequal-image morphisms, that every ordered binary pair is witnessed at each distance \(d=1,2,3\) inside \(\sigma^3(0)\). It also checks the following four finite identities for every such morphism and \(r\in\{0,1,2,3\}\):
\[\bigcup_{t=0}^3 \bigl\{(\sigma(a)_t,\sigma(b)_{(t+r)\bmod4}):a,b\in\{0,1\}\bigr\}=\{0,1\}^2.\]
Both checks enumerate 15 explicitly defined morphisms and at most four choices in each finite variable, so they are exhaustive finite lemmas, not assumptions based on large samples. To induct, let \(d=4q+r\ge4\), with \(0\le r<4\) and \(q\ge1\). For positions \(4j+t\), the separated pair equals
\[(\sigma(x_j)_t,\sigma(x_{j+q+\lfloor(t+r)/4\rfloor})_{(t+r)\bmod4}).\]
The two relevant distances in the source word, \(q\) and \(q+1\), are both positive and strictly smaller than \(d\). By induction their pair sets are full. Applying the checked finite identities proves \(P(d)=\{0,1\}^2\). This is a complete induction for every \(d\ge1\).

**2. Boundary count formula.** Fix \(n=4q+r\), where \(q\ge1\) and \(0\le r<4\). Each complete substituted block has two ones. Denote by \(\mathrm{pre}_h(w)\) and \(\mathrm{suf}_h(w)\) the numbers of ones in the first or last \(h\) symbols of \(w\), and set \(B_0=u,B_1=v\). A factor beginning at substituted-block offset zero has exactly
\[2q+\mathrm{pre}_r(B_b)\quad(b\in\{0,1\})\]
ones. This set is fully attainable because both letters occur in the fixed point. For offset \(t\in\{1,2,3\}\), put \(h=t+r\), \(\delta=\mathbf1_{\{h>4\}}\), \(h'=h-4\delta\). Its number of ones is exactly
\[2(q-1+\delta)+\mathrm{suf}_{4-t}(B_a)+\mathrm{pre}_{h'}(B_b).\]
The two endpoint source symbols are at positions separated by \(q+\delta\); by step 1 all four ordered choices \((a,b)\in\{0,1\}^2\) occur. Therefore the union of the displayed, explicit finite sets gives precisely all possible one-count values at length \(n\). Their extrema depend on \(r\) and on \(u,v\), not on \(q\). Sliding a length-\(n\) window changes its number of ones by at most one; hence every integer between the minimum and maximum is attained and \(a_x(n)=1+\max C-\min C\). Enumerating the three starting words, all six second images, and four residues gives exactly the table above, with no appeal to finite sampling for an infinite assertion.

**3. The initial lengths and coincident images.** When \(n\in\{1,2,3\}\) and \(u\ne v\), a length-\(n\) factor lies inside \(\sigma(a)\sigma(b)\), for some adjacent pair \((a,b)\). By step 1 all four adjacent pairs occur; hence enumerating their length-\(n\) boundary factors is complete. This gives the exceptional \(a_x(1)=2\), and the tabulated values for lengths two and three. If \(u=v\), then \(x=uuu\cdots\) is periodic with period dividing four; comparing its four rotations gives the first two rows of the table for all \(n\ge1\).

## Verification
Run `python3 verify.py` from the directory containing the included checker. The program exhaustively checks the 45 base pair predicates and 60 finite pair-lifting predicates (15 unequal morphisms, four residues). It independently compares the exact boundary formula or periodic calculation with all 1,152 direct factor-complexity calculations for lengths 1 through 64 over all 18 morphisms. The result is `VERIFY_OK morphisms=18 theorem_pair_base_checks=45 theorem_pair_lift_checks=60 factor_length_checks= 1152`. Finite factor sampling corroborates, but the infinite proof is the induction and boundary identity above.

## Relationship to prior work
Rigo, Stipulanti and Whiteland prove that the abelian-complexity function for any Parikh-collinear fixed point is automatic and give an effective automaton procedure (Theorem 3, [1]). They explicitly ask whether Parikh-constant fixed points always have ultimately periodic abelian complexity (Section 6). The present result is a closed-form classification for all balanced binary four-uniform images, including a new all-positive-displacements pair-saturation lemma and an instance where complexity five occurs at every positive multiple of four. The general automaticity theorem ensures computability, but does not itself state the 18 explicit functions or the pair-saturation lemma. This does not establish global priority against unindexed equivalent derivations.

## Limitations
The periodicity assertion is only for this restricted 18-morphism family, not for general Parikh-constant morphisms. The result is an explicit small-family classification, not a resolution of the general eventual-periodicity question. Exact formulas use positive factor lengths; a length-zero convention is not specified. The certificate only exhausts stated finite base identities and finite sample comparisons; the symbolic induction supplies all infinite quantifiers.

## References
[1] M. Rigo, M. Stipulanti, M. A. Whiteland, *Automatic Abelian Complexities of Parikh-Collinear Fixed Points*, arXiv:2405.18032 (first posted 2024-05-28), Theory of Computing Systems 68 (2024), 1622–1639, doi:10.1007/s00224-024-10197-5. See Theorem 3 and Section 6.

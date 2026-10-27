# Cyclic color symmetry permits only shifts and traffic lifts on proper three-colorings

## Finding

Let \(X\subseteq(\mathbb Z/3\mathbb Z)^{\mathbb Z}\) consist of all proper three-colorings of the integer path: \(x_i\ne x_{i+1}\) for every \(i\in\mathbb Z\). Among all centered-radius-one cellular automata \(F:X\to X\) satisfying \(F(x+c)=F(x)+c\) for every uniform color rotation \(c\in\mathbb Z/3\mathbb Z\), there are exactly **15 distinct maps**. They consist of the **nine automorphisms** \(x\mapsto\sigma^j x+c\), with \(j\in\{-1,0,1\}\) and \(c\in\mathbb Z/3\mathbb Z\), and **six nonsurjective maps**, comprising three color translates of each of two local traffic lifts.

For the two traffic maps, define \(u_i=x_i-x_{i-1}\) and \(v_i=x_{i+1}-x_i\), represented by signs \(\pm1\pmod3\). The two maps are
\[
T_+(x)_i=x_i+\mathbf1_{(u_i,v_i)=(1,-1)}\pmod3,
\qquad T_-(x)_i=x_i-\mathbf1_{(u_i,v_i)=(-1,1)}\pmod3.
\]
Their coordinatewise differences are precisely the elementary binary cellular automata Rule 184 and Rule 226, respectively. If equivariance is strengthened to **all six permutations of the three colors**, only the three uncolored coordinate shifts remain.

## Assumptions and scope

All configurations are bilateral and carry the product topology. The shift is \((\sigma x)_i=x_{i+1}\). A centered-radius-one cellular automaton is defined by a rule \(f(a,b,c)\) on the 12 proper triples \(a\ne b\ne c\) (the two inequalities are adjacent inequalities, and \(a=c\) is allowed). No choice on inadmissible triples is relevant. A *uniform color rotation* adds the same element of \(\mathbb Z/3\mathbb Z\) at all coordinates. The classification is only for these local maps and this symmetry; larger radii are not addressed.

## Proof

**Step 1: all cyclic-equivariant local rules.** Every proper triple \((a,b,c)\) determines signs \(u=b-a\) and \(v=c-b\) in \(\{1,-1\}\) modulo three. Global color rotation acts transitively and freely on the three triples with each fixed ordered sign pair. Therefore every equivariant rule is uniquely of the form
\[
 f(a,b,c)=b+g(u,v)\pmod3,
 \qquad g:\{\pm1\}^2\longrightarrow\mathbb Z/3\mathbb Z.
\]
There are exactly \(3^4=81\) candidate functions \(g\).

**Step 2: preservation criterion.** Any triple of consecutive edge signs \((u,v,w)\in\{\pm1\}^3\) occurs in a bilateral proper coloring. The adjacent output difference under \(F\) is
\[
 v+g(v,w)-g(u,v)\pmod3.
\]
Consequently, \(F(X)\subseteq X\) if and only if this expression is nonzero for **all eight** sign triples. Exhausting the four entries of \(g\) over \(\{0,1,2\}\) gives precisely the 15 functions obtained by adding a constant to each of the following five representatives. Their entries are ordered as \((u,v)=(-1,-1),(-1,1),(1,-1),(1,1)\):

| Representative | Four entries of \(g\) | Induced binary edge rule |
| --- | --- | --- |
| identity | \((0,0,0,0)\) | 204 |
| \(\sigma\) | \((2,1,2,1)\) | 170 |
| \(\sigma^{-1}\) | \((1,1,2,2)\) | 240 |
| \(T_+\) | \((0,0,1,0)\) | 184 |
| \(T_-\) | \((0,2,0,0)\) | 226 |

Adding \(0,1,2\) to all four entries of a representative produces three distinct functions in each class, and the five classes are disjoint. The eight universal constraints and all 81 cases can be reproduced with the standalone `verify.py`; the computation is exhaustive because the complete space of equivariant local functions has only 81 members. A second check loops independently over all admissible four-color input words, using no algebraic sign criterion, and finds exactly the same 15 functions.

**Step 3: edge factors and surjectivity.** Let \(d:X\to\{0,1\}^{\mathbb Z}\) record the edge signs, with symbol \(1\) for increment \(+1\) and symbol \(0\) for increment \(-1\). Every binary edge sequence has exactly three coloring lifts, related by uniform color rotation. The output increment formula in Step 2, evaluated at the five representative functions, is exactly the Wolfram local rule with code 204, 170, 240, 184 or 226 as shown. A constant added to \(g\) does not change its induced edge rule.

The maps induced by Rules 170, 204 and 240 are coordinate shifts and thus onto. They lift to the nine explicitly invertible maps \(x\mapsto\sigma^j x+c\). The image of Rule 184 omits the binary word `1100`: starting from all four two-bit predecessor states and reading this output word, the reachable-state cardinalities are successively \(4,3,1,1,0\). Rule 226 analogously omits `0011`, with the same cardinalities. Therefore the six traffic lifts are not surjective on \(X\). The proof does not infer nonsurjectivity merely from finite periodic-ring experiments: the missing binary words define open cylinders with no global preimage.

**Step 4: full color-permutation symmetry.** The cyclic rotations and one reflection generate the entire permutation group \(S_3\). Among the 15 preserving maps, commuting with a reflection removes all nonzero constant color rotations and both traffic families (the reflection exchanges peak and valley edge patterns). The surviving maps are exactly \(\sigma^{-1}\), the identity and \(\sigma\). Direct local checking of all six symbol permutations confirms this reduction.

## Verification

Run `python3 verify.py` with Python 3; no nonstandard packages are required. It exhausts all \(3^4\) cyclic-equivariant local rules both through the eight sign constraints and by independent four-color input checks. It compares the five representative edge rules with Wolfram codes, checks the missing-word subset transitions and verifies complete \(S_3\)-symmetry on all admissible triples. Independent cyclic finite-word enumeration on rings of length three through seven is an additional consistency check, not a substitute for the all-configuration argument. The expected output begins `VERIFY_OK`.

## Relationship to prior work

Salo and Törmä's *Color Blind Cellular Automata* studies permutation-centralizing cellular automata and gives general extension and characterization results, including for subshifts. The present classification specializes to **proper three-colorings under only the cyclic subgroup** and determines the exact low-radius centralizer, its binary edge factors and its surjectivity spectrum; those precise conclusions are not stated in the inspected relevant sections of that source. Their earlier *On Shift Spaces with Algebraic Structure* studies general algebraic subshift methods rather than this coloring constraint. Fukś's original Rule 184 work establishes the classical traffic automaton; Rule 184 itself is not claimed to be new. Its occurrence here as one of the **only two possible nonlinear induced rules**, together with the complete 15-map/9-surjection classification, is the claim assessed here. Related binary traffic-image results alone do not imply this complete lifting classification.

## Limitations

The theorem only treats centered-radius-one maps commuting with uniform cyclic color rotations. No classification is claimed for arbitrary local radii, other proper-coloring alphabets, or arbitrary color-symmetric maps. The older literature on general symbol-permutation centralizers and Rule 184 is substantial; an unindexed equivalent local classification cannot be excluded by search alone. This result has not undergone independent scientific audit.

## References

1. H. Fukś, *Solution of the Density Classification Problem with Two Cellular Automata Rules*, arXiv:comp-gas/9703001v1, first publicly submitted 1997-03-07, especially Section II.
2. V. Salo and I. Törmä, *On Shift Spaces with Algebraic Structure*, arXiv:1203.6795v1, first publicly submitted 2012-03-30.
3. V. O. Salo and I. A. Törmä, *Color Blind Cellular Automata*, Automata 2013, Lecture Notes in Computer Science 8155, pp. 139–154; expanded Journal of Cellular Automata 9 (2014), pp. 477–509; doi:10.1007/978-3-642-40867-0_10. An author-hosted complete open-access text was inspected.

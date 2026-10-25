# Sharp threefold periodic lifting for the Rule 22 image

## Finding
Let \(\Phi:\{0,1\}^{\mathbb Z}\to\{0,1\}^{\mathbb Z}\) be elementary cellular automaton Rule 22: \((\Phi x)_i=1\) precisely when \((x_{i-1},x_i,x_{i+1})\) is one of `001`, `010`, `100`. Let \(Y=\Phi(\{0,1\}^{\mathbb Z})\). For every integer \(n\ge1\) and every \(y\in Y\) satisfying \(\sigma^n y=y\), there is a preimage \(x\) with \(\Phi x=y\) and \(\sigma^{kn}x=x\) for some \(k\in\{1,2,3\}\). Moreover:

1. If \(y\) contains a zero and a one, then \(k\in\{1,2\}\) suffices. The same conclusion holds for \(y=0^{\mathbb Z}\).
2. For \(y=1^{\mathbb Z}\), an \(n\)-periodic preimage exists if and only if \(3\mid n\); otherwise the least positive multiplier \(k\) is exactly \(3\). Every preimage of this constant output is three-periodic with a spatial translate of `001` as its period.
3. The factor \(2\) is sometimes required: the periodic output \((001)^{\mathbb Z}\) has no three-periodic preimage but does have a six-periodic preimage. Thus both nontrivial multipliers in the theorem occur.

Here an \(n\)-periodic configuration means one fixed by \(\sigma^n\), not necessarily of least period \(n\). The theorem concerns spatial periods of **one-step preimages**, not temporal periods under iteration of \(\Phi\).

## Assumptions and scope
The alphabet is binary, spatial coordinates range over all integers, \(\sigma\) is the spatial shift, and there are no boundary conditions or probabilistic assumptions. The claim is restricted to the image \(Y\); an arbitrary periodic binary configuration not in \(Y\) need not have any preimage. The period multiplier is relative to a specified \(n\), even when \(y\) has smaller least spatial period.

## Proof
Use the four two-bit overlap states \(00,01,10,11\), encoded as \(0,1,2,3\). A local input triple \(abc\) gives a directed edge from \(ab\) to \(bc\), labeled by its Rule 22 output. Encode a relation as a tuple of four bitmasks recording its target sets. The exact relations for output symbols \(0\) and \(1\), respectively, are
\[
L_0=(1,8,2,12),\qquad L_1=(2,4,1,0).
\]
Composition is Boolean matrix multiplication. For a finite binary word \(w=w_0\cdots w_{n-1}\), put \(R(w)=L_{w_0}\cdots L_{w_{n-1}}\). The trace of \(R(w)^k\) is nonzero if and only if the repeated output \(w^{\mathbb Z}\) has an input period dividing \(kn\). The forward implication concatenates a closed path of length \(k\) in the return relation; the reverse implication reads the periodic antecedent as a closed labeled de Bruijn path. In particular, \(w^{\mathbb Z}\in Y\) exactly when the four-vertex graph of \(R(w)\) has a directed cycle, in which case some \(k\le4\) suffices.

It remains to rule out a genuinely new fourfold requirement and to classify threefold requirements. These are finite exact statements about the two generated relations. Starting from the identity relation, repeatedly right-multiply every new relation by \(L_0\) and \(L_1\), and stop at closure. The attached `verify.py` implements this computation using only integer bit operations. Exactly \(2375\) distinct relations are reached. For each it determines the first \(k\in\{1,2,3,4\}\) with \(\operatorname{tr}(R^k)>0\), or records no such \(k\). None has first return at \(4\). Exactly two relations have first return at \(3\): \(L_1\) and \(L_1^2\).

To check that a mixed word cannot represent either exceptional relation, retain a second Boolean flag recording whether any output \(0\) has occurred in the prefix. Breadth-first closure of this augmented deterministic finite graph has exactly \(2375\) reachable states and no state with the flag true and first return \(3\). This is an exhaustive finite-state induction, not an enumeration up to any maximum word length. Consequently, every nonconstant periodic image word, and also every word containing \(0\), has a return at multiplier \(1\) or \(2\).

Finally, \(L_1\) is exactly the directed three-cycle on states \(0\to1\to2\to0\), with state \(3\) having no outgoing labeled-one edge. Thus \(R(1^n)=L_1^n\) has a loop precisely when \(3\mid n\); otherwise its first return multiplier is \(3\). The cycle spells the three shifted repetitions of `001`, proving the additional description of all antecedents of the all-one output. Direct multiplication for `001` gives zero trace at multiplier \(1\) and positive trace at multiplier \(2\), proving sharpness. All arithmetic in the finite certificate is exact.

## Verification
Run `python3 verify.py` (Python 3 standard library only). The program independently reconstructs the local rule and both overlap relations, enumerates the entire \(2375\)-element generated Boolean relation semigroup until closed under both letters, checks its exhaustive period-multiplier classification and the augmented flag invariant, and brute-force cross-checks same-period antecedence on all cyclic words of lengths \(1\) through \(10\) (\(2046\) words). It prints a `VERIFY_OK` confirmation after all assertions pass. The machine computation is a finite, terminating exhaustive certificate; the preceding reduction explains why it proves a statement for every positive period rather than only the checked sample.

## Relationship to prior work
The dynamics of the Rule 22 ('exactly one') cellular automaton and its finite-seed behavior were developed in earlier work by Badii and Politi (1997) and Gravner and Griffeath (2010). Martínez and collaborators (2019) analyze de Bruijn and subset diagrams, including Garden-of-Eden configurations. Mariot and Leporati (2015) study periodic preimage periods for *linear bipermutive* cellular automata, while Salo (2022) formulates general periodic-point obstructions to cellular-automaton regularity. The present theorem is an evaluated **uniform bound and exact third-multiplier classification for the nonlinear, nonsurjective Rule 22**, neither a classification of its limit set nor the general decidability theorem. Existing graph and semigroup methods make this finite case in principle decidable; no claim is made to have invented those methods.

## Limitations
The closed semigroup comprises \(2375\) relations, so the proof relies on an explicitly supplied reproducible finite computation. The theorem does not enumerate all words requiring the multiplier \(2\) or provide a closed generating function for them. It concerns the one-step image only. Bibliographic searching cannot exclude an earlier unindexed specialization of the general finite-graph method; independent priority and independent mathematical audits have not been performed.

## References
- R. Badii and A. Politi, *Thermodynamics and Complexity of Cellular Automata*, Physical Review Letters 78 (1997), 444–447. DOI: 10.1103/PhysRevLett.78.444. https://www.dora.lib4ri.ch/psi/islandora/object/psi:73148
- J. Gravner and D. Griffeath, *The One-Dimensional Exactly 1 Cellular Automaton: Replication, Periodicity, and Chaos from Finite Seeds*, Journal of Statistical Physics 142 (2011), 168–200. DOI: 10.1007/s10955-010-0103-9. First online 2010-12-10.
- L. Mariot and A. Leporati, *On the Periods of Spatially Periodic Preimages in Linear Bipermutive Cellular Automata*, AUTOMATA 2015. https://lucamariot.org/publication/ml-automata-2015/
- G. J. Martínez, A. Adamatzky, R. Hoffmann, D. Désérable, and I. Zelinka, *On Patterns and Dynamics of Rule 22 Cellular Automaton*, Complex Systems 28 (2019), 125–174. DOI: 10.25088/ComplexSystems.28.2.125.
- V. Salo, *On von Neumann regularity of cellular automata*, arXiv:2209.13373 (2022). https://arxiv.org/abs/2209.13373

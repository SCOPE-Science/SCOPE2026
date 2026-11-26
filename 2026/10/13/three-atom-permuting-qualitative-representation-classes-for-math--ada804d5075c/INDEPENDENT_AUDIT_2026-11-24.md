# Independent mathematical audit

## correctness

PASS

The frozen three-class finding is false: seven-point representations extend uniquely, but arbitrary deletions of an eight-point representation need not retain any given triangle witness. The frozen verify.py at lines 278–314 canonicalizes every restricted colouring without testing coverage in any restriction. In the affine representative on F7∪{∞}, colour(x,y)=(x+y)/2 for finite endpoints and colour(∞,x)=x. The non-progression colour triple {2,4,5} occurs only on {0,1,3}, and deletion of 0 destroys it. The complete repaired claim has one class at each size. On eight points the proper colouring is a one-factorization. If two factors give two 4-cycles only their four diagonals close triangles with both colours, so fewer than the required five third colours can appear. Thus qualitative implies perfect. In the explicit affine construction every triple of distinct colours a,b,c occurs on the unique finite triangle with vertices a+b−c,a+c−b,b+c−a. It is therefore qualitative, and uniqueness of the perfect factorization gives the converse and the eight-point class. An extra witness through ∞ exists exactly for a progression triple; that witness is disjoint from the finite one. Each of the seven finite vertices lies on nine progression and six non-progression finite triangles. Hence the finite deletions have exactly 29 of the 35 required triples, while the ∞ deletion has 35. The extension theorem then gives a unique seven-point class. Any automorphism up to colour relabelling fixes ∞ and induces a midpoint-preserving permutation of F7, necessarily one of the 42 affine permutations; these have vertex orbits of sizes 1 and 7. Independent exact replay in /workspace/repairs/5/verify.py checked the full fixed-factor exact-cover census (416 instances, six vertex-relabelled classes), Hamiltonian-pair and full-coverage equivalence in every instance, the group order and orbits, and restriction counts [29,29,29,29,29,29,29,35]. The general seven-to-eight extension is a separate primary-source input. The corrected finding, slogan and scientific verification notes and code are under /workspace/repairs/5/; the frozen self-review is evidence of the original error, not validation of the repair.

## originality

PASS

For the corrected result, the affine examples at both sizes, the quasigroup characterization and extension theorem, and the classical perfect factorization and K8 census are prior inputs. The supported distinct claim is the coverage/perfectness bridge at order eight, the associated uniqueness at both base sizes and the precise failure of witness preservation for the seven non-fixed deletions. The bounded checks found no source already giving that restricted classification or its equivalent. This is not an originality pass for the false three-class claim.

## value

PASS

At K8, the first order where nonisomorphic one-factorizations branch, the qualitative test singles out the perfect one. The repaired result answers the natural small-case moduli question at both allowed base sizes and determines exactly when the extension construction can be reversed without losing qualitative witnesses. This is stronger than checking a single example or just recomputing the six graph factorizations: one of the two actual deletion orbits is excluded from the algebra's moduli despite being a proper colouring, through a concrete and sharp 29-versus-35 obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.

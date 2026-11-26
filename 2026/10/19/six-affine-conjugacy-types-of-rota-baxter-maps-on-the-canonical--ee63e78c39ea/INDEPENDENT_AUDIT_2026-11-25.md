# Independent mathematical audit

## correctness

PASS

For P=R+p expand the affine bracket identity, evaluating the constant, one-variable and mixed terms at zero separately. This yields R(p)=0, commutation with ad_p, R²=R, and the weight −1 bilinear identity; evaluating at zero and subtracting is valid also in characteristic two and over F₂. For a projection the bilinear identity is equivalent to closure of both its image and kernel under brackets, since all mixed terms cancel. The Heisenberg bracket on the central quotient is a nondegenerate alternating determinant form, so precisely the planes containing the center are subalgebras. In rank one a complementary image line meets the center trivially, so a permitted kernel translation must centralize it and is then central. In rank two the image plane already contains the bracket and every complementary-line translation is allowed. An affine automorphism has linear Lie-automorphism part and a central translation, by the bracket identity with one input zero. Its action sends p to Gp+(I−GRG⁻¹)t. The linear group aligns the ordered quotient directions and the central shears align the chosen lifts. Central translations remove the rank-one translation but do nothing to rank two, where the line stabilizer is transitive on nonzero translations. Constants split into central and noncentral. This gives the listed six distinct orbits and idempotence. Over F_q there are q+1 planes containing the center and q² complementary lines per plane; splitting the q allowed rank-two translations into zero and nonzero gives the six stated orbit sizes and total. An independent exact finite check scanned all linear maps and translations at q=2,3, testing the original identity on zero and basis vectors in both slots (bi-affine residual), then on all inputs for each accepted map. It also conjugated the state permutations under all affine bracket automorphisms found by direct evaluation. The counts were 57 and 244 with orbit lists (2,6,24,12,12,1) and (3,24,108,36,72,1). The supplied standard-library checker was inspected, not executed; its package replay path is `python3 artifacts/verify.py`. The finite samples are corroboration, not the proof for arbitrary fields.

## originality

PASS

Credit the explicit six-orbit classification under the full affine automorphism group and the characteristic-free finite-field census. The image/kernel/translation parameterization and equivalence framework in characteristic zero are already in Han et al.; the new scope is not general affine Rota–Baxter factorization. The checked linear censuses include non-idempotent linear parts and do not classify translated operators or their conjugacy.

## value

PASS

The three-dimensional Heisenberg algebra is the first nonabelian nilpotent Lie algebra, and the full affine equivalence problem is distinct from classifying linear solutions. The calculation determines explicitly when central translations remove a parameter and when a second affine orbit survives; it gives exact orbit-field counts, including in characteristic two, where the cited general characteristic-zero theorem cannot be invoked. This is a usable complete model case rather than just a new notation for the general reduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.

# Independent mathematical audit

## correctness

PASS

The theorem uses genuine fixed points of geometric realization, with barycentric weights constant on H-orbits, not just vertexwise fixed simplices. The orbit incompatibility graph exactly represents admissible fixed simplex supports. For rotation r^d, the orbits are residue classes modulo d; if d divides n they contain antipodal chord edges and all are forbidden. Otherwise d|2n forces d=2m, n congruent m mod d, giving the quotient Möbius graph M_2m (including M2=K2). Adjoining a reflection reduces to i->b-i on this quotient. Even b yields an m/2-centred pair of ladder rails with t=ceil(m/2) rungs; odd b deletes its two rim-edge orbits and, if needed, an antipodal one, giving t=max(0,floor(m/2)-1). Neighborhood-folds N(a1) subset N(b2) and then N(b1) subset N(a2) reduce Ind(L_t) to suspension of Ind(L_(t-2)), with L1 and L2 both S0, yielding S^floor((t-1)/2). Independent orbit enumeration directly tested all divisors d and reflection cosets for 4<=n<=40 and found the specified empty/Möbius/ladder graphs, including edge parity and small cutoffs. The Smith equality criterion uses Agarwal–Basak’s source theorem: ambient total mod-two Betti 4 when n≡2 mod4, 2 otherwise, whereas both reflection fixed spheres have total Betti 2; hence equality iff n not ≡2 mod4. Finite tests are corroboration, not an all-size proof.

## originality

PASS

Best-of-knowledge PASS. The closest same-graph 2026 primary paper was read in substantive full-text sections and determines ambient independence complexes, not all dihedral-subgroup geometric fixed spaces. The nearest published character record gives rational representation traces, which cannot specify individual fixed-space homotopy types. The new explicit subgroup-wise orbit graphs and Smith equality pattern are not logically entailed by those statements.

## value

PASS

All subgroup fixed-space homotopy types of a canonical D_2n action on a natural infinite family are determined by exact PL smaller Möbius and open-ladder models. The periodic Smith-equality criterion is a motivated global symmetry phenomenon; ambient Betti numbers alone cannot provide it. This is a natural complete classification, not an arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.

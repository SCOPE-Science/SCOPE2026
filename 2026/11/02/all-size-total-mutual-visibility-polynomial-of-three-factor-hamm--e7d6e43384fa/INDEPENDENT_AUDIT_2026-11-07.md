# Independent mathematical audit

## correctness

PASS

For G=Ka □ Kb □ Kc, a,b,c>=2, use published theorem that total mutual-visible iff no selected pair at Hamming distance exactly 2. Adjacent selected vertices must lie on same coordinate line throughout each connected induced component; otherwise two at distance 2. Distinct components differ in all three coordinates, hence use disjoint coordinate-label supports. This gives a canonical labeled mixed-species SET decomposition (unused labels plus singleton triples plus coordinate lines length>=2) with EGF exp(x+y+w+zxyw+yw(exp(zx)-1-zx)+xw(exp(zy)-1-zy)+xy(exp(zw)-1-zw)). Mark one first-coordinate label to obtain the displayed finite positive recurrence. For a>=b>=c>=5, three components each varying in distinct axes attain a+b+c-6, and choices of ordered fixed labels yield a(a-1)b(b-1)c(c-1) maxima in one orbit. When c=2,b>=3, two axis-lines attain a+b-2, count 2ab. Independent integer recurrence generated exact polynomials (2,2,2): 1+8z+16z²; (3,3,3):1+27z+189z²+387z³+162z⁴, and (4,4,4), and top (5,5,5)=8000. Entire algebraic bijection proves all parameters; finite regressions only confirm small cases.

## originality

PASS

PASS best knowledge for full all-cardinality Hamming 3-factor EGF, recurrence, exact extremal multiplicities and orbits, not for published distance-two criterion or known maximum sizes. Full primary Bujtás–Klavžar–Tian 2023 paper inspected: Section 3 has a related component/base-edge decomposition already credited, but no EGF. Full 2025 visibility-polynomial paper supplies general inclusion-exclusion technique but not this explicit enumerator. Potential equivalence with independently studied three-partite hypergraph induced matching polynomials remains risk.

## value

PASS

Gives an exact labeled counting polynomial for a natural graph invariant, improving known scalar optimum into all-size distribution and precise optimal multiplicities; useful as benchmark and structural enumeration for Hamming visibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.

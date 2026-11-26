# Independent mathematical audit

## correctness

PASS

For B=D^{-1/2}AD^{-1/2}, the four-cell quotient has spectrum ±1,±c, where c²=pq/((p+1)(q+1)); the complement comprises the two within-side zero-sum spaces at eigenvalue 0 of B. The positive normalized-Laplacian zero mode pins phase to +1 and forces equal degree; projected transfer forces strong cospectrality. At eigenvalue 1 of H the zero-sum leaf projections exclude cross-side pairs unless p=q=1, and sibling pairs unless their side has size two. Equal-degree hubs have p=q=r. The balanced reflection-odd B block is [[0,√(r/(r+1))],[√(r/(r+1)),−1/(r+1)]], with eigenvalues c and −1; both components of its eigenvectors are nonzero. It requires negative phases at 1/(r+1) and 2 under H, incompatible because the latter phase is an even power of the former. This also excludes the P4 end pair. For the remaining size-two leaf pair, the symmetric eigenmodes all have positive sign; the antisymmetric eigenmode at H=1 has negative sign. This is exactly simultaneous odd-π matching for t and ct. Irrational c gives arbitrarily late approximate matches by circle density and no exact ones. Rational c is equivalent to q(q+1)=6h²; the positive Pell equation (2q+1)²−24h²=1 has fundamental unit 5+√24. Its first coordinate is 1 modulo 4 along all positive powers, making q even and c=2h/(q+1) even-over-odd in lowest terms. Even limiting odd-π matching then contradicts equality of the phases raised to the numerator and denominator powers. The symmetric case follows by swapping hubs. An independent bounded Python/NumPy check used the four-cell random-walk quotient (144 cases), a direct square scan through 100000 (2, 24, 242, 2400, 23762), and the symmetric leaf return via its second spectral moment, giving fidelity above 0.99999999 at sampled odd multiples of π for q=1,3,4,5,6. These are checks only; the spectrum, pair exclusions, density and Pell proof establish the full claim. The original replay path is verify.py, inspected but not executed.

## originality

PASS

The supported distinct claim is the exhaustive normalized-Laplacian double-star classification, including its explicit Pell obstruction. Published twin and tree criteria cover much of the machinery and a prior indexed result covers the even-order PST subcase. The closely matching adjacency classification has different answers. No inspected statement provides the entire normalized double-star spectrum/transfer analysis or the parameter classification as a direct instance without the family-specific calculations and exclusions.

## value

PASS

Completely classifies all vertex pairs in a canonical infinite family (all diameter-three trees), with an infinite arithmetic exceptional set and a distinction between approximate and exact transfer. The normalized classification genuinely differs from the studied ordinary adjacency one; the family-specific Pell exclusion and non-twin checks, rather than a restatement of the general twin criterion, provide the value.

The dated certificate retains the supplied scientific assessment, sources and limitations.

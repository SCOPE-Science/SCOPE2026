# An infinite 7-adic obstruction for cyclic consecutive-integer concatenations

## Finding
For every integer \(t\ge0\), let \(d=42t+5\), and define \(m=10^{d-1}+8\). Write \(C_m\) for the positive decimal integer formed by concatenating the decimal expansions of \(1,2,\ldots,m\), and \(L_m\) for its number of digits. Then
\[
C_m\equiv14\pmod{49},\qquad L_m\equiv0\pmod{42}.
\]
Every cyclic permutation of the ordered list \(1,2,\ldots,m\) therefore produces a decimal concatenation divisible by \(7\) but not \(49\). None is a perfect \(k\)-th power for any integer \(k\ge2\).

## Assumptions and scope
The decimal words used for each positive integer have no leading zero. A cyclic permutation means rotating the ordered list of integer blocks without permuting the entries arbitrarily. The theorem holds for every integer \(t\ge0\) and covers an infinite sequence of strictly increasing indices. These indices satisfy \(m\equiv0\pmod9\), so the known index-exclusion criterion for the residues \(2,3,5,6\pmod9\) does not apply.

## Proof
Work modulo \(49\). Appending a positive integer \(k\) having \(e\) digits transforms the current concatenation residue \(v\) to \(10^e v+k\pmod{49}\). For a fixed digit width \(e\), track the pair \((v,k)\) using the affine transformation
\[
T_e(v,k)=(10^e v+k,\ k+1)\pmod{49}.
\]
The block of all \(e\)-digit positive integers applies \(T_e\) exactly \(9\cdot10^{e-1}\) times, beginning at \(k=10^{e-1}\). Consequently its action on the previous residue is an affine map \(v\mapsto a_e v+b_e\pmod{49}\). It increases the decimal length by \(9e10^{e-1}\pmod{42}\).

The order of \(10\) modulo \(49\) is \(42\). For each \(e\), the reduction of \(T_e^{42}\) modulo \(7\) is the identity: the diagonal eigenvalues have orders dividing \(6\), while the largest unipotent Jordan block has size at most three, and \(42\) is divisible by \(7\). Hence \(T_e^{42}=I+7K\pmod{49}\), so
\[
T_e^{294}=I\pmod{49}.
\]
For \(e\ge2\), the residues of \(10^e\) modulo \(49\), of \(10^{e-1}\) modulo \(49\), and of \(9\cdot10^{e-1}\) modulo \(294\) repeat when \(e\) is increased by \(42\). (Modulo \(49\) this follows from the order \(42\); modulo \(6\), positive powers of \(10\) are constant.) Therefore the entire digit-width-block affine map and its length increment repeat with period \(42\) for \(e\ge2\).

Compute the composition of the 42 affine maps for digit widths \(2,3,\ldots,43\), together with their length increments. Exact modular exponentiation gives the triple
\[
(a,b,\ell)=(1,0,0)\quad\text{in}\quad (\mathbb Z/49\mathbb Z)^2\times\mathbb Z/42\mathbb Z.
\]
The included standalone program performs this finite calculation explicitly; it checks every individual 42-period comparison and the full identity. Since the block maps are invertible and repeat with period 42, the 42-step identity applies at every later digit width. It follows that the concatenation residue and total length at the end of the \((42t+4)\)-digit block equal those at the end of the four-digit block for every \(t\ge0\).

Now append exactly the first nine \((42t+5)\)-digit integers, beginning with \(10^{42t+4}\). Their affine operation modulo \(49\) and length increment modulo \(42\) are again the same as the corresponding nine five-digit integers, because both the digit width and the starting value agree in the requisite residue classes. Exact modular arithmetic gives
\[
(C_{10008},L_{10008})\equiv(14,0)\pmod{(49,42)}.
\]
Combining the periodic block calculation and this nine-integer calculation proves the two congruences for every specified \(m\).

Finally, a cyclic rotation of a decimal word of length \(L\), moving a prefix of \(h\) digits to the end, has value
\[
C'=10^h C+P(1-10^L),
\]
where \(P\) is the numerical value of that prefix. Since \(42\mid L\), one has \(10^L\equiv1\pmod{49}\). Thus \(C'\equiv10^h C\pmod{49}\). Because \(10\) is a unit modulo \(49\) and \(C\equiv14\pmod{49}\), every rotation has exactly one factor \(7\). A perfect power of exponent at least two cannot have this valuation. Rotations at integer-block boundaries are among these decimal-word rotations, proving the assertion.

## Verification
Run `python3 verify.py` with Python 3 standard library. The program checks the affine composition algorithm, its 42-periodicity across all 42 digit classes, the identity of the 42-width superblock, and the pair \((14,0)\) for the first index. An independent direct scan of the decimal digits of all integers from \(1\) to \(10008\) yields the same pair. The infinite extension follows from the stated finite-state congruence argument, not extrapolation from examples.

## Relationship to prior work
Marco Ripà studied Kashihara's question concerning perfect powers among cyclic rearrangements of concatenations of consecutive integers. The source proves a 3-adic exclusion for indices congruent to \(2,3,5,6\pmod9\), and supplies finite computational exclusions for small indices. The present indices are all divisible by \(9\), hence are outside that criterion. The new assertion is the uniform infinite 7-adic obstruction for these cyclic rotations; it does not address unrestricted permutations of all the blocks. OEIS entries A001292 and A352991 supply the sequence definitions and references.

## Limitations
This is an infinite subfamily of the cyclic-permutation problem, not a resolution of Kashihara's general conjecture. No statement is made about noncyclic rearrangements, about all indices divisible by nine, or about perfect powers in the broader all-permutations sequence. The block-composition identity is a finite certificate implemented with ordinary exact modular arithmetic; no external independent mathematical audit has been conducted.

## References
- Marco Ripà, *On some open problems concerning perfect powers*, arXiv:2205.10163, first submitted May 19, 2022, https://arxiv.org/abs/2205.10163.
- OEIS A001292, cyclic rearrangements of consecutive-integer decimal concatenations, https://oeis.org/A001292.
- OEIS A352991, all distinct permutations of consecutive-integer decimal concatenations, https://oeis.org/A352991.

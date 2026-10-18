# Exact two-term dyadic power-sum distributions and their Haar image measure

## Finding

Fix any integer \(t\ge2\), and put \(d=2^t\) and \(h=t+2\). Let \(R_{t,n}(r)\) denote the number of **ordered** pairs of residues \(x,y\pmod{2^n}\) for which
\[
x^d+y^d\equiv r\pmod{2^n}.
\]
The exact target-by-target distribution is as follows. In every clause write \(q=2^n\), interpret \(r\) as a residue modulo \(q\), and use the clauses in their stated ranges.

* At \(n=0\), \(R_{t,0}(0)=1\).
* At \(n=1\), both target residues have count \(2\).
* If \(2\le n<h\), the counts for \(r=0,1,2\) are respectively \(q^2/4,q^2/2,q^2/4\); all other target residues have count zero.
* If \(n\ge h\) and \(r\equiv1\pmod{2^h}\), then \(R_{t,n}(r)=2^{t+1}q\).
* If \(n\ge h\) and \(r\equiv2\pmod{2^h}\), then \(R_{t,n}(r)=2^tq\).
* If \(h\le n<d\), the remaining nonzero count is \(R_{t,n}(0)=q^2/4\).
* If \(n\ge d\), every target not covered by the preceding two congruence classes satisfies
\[
R_{t,n}(r)=
\begin{cases}
2^{2(d-1)}R_{t,n-d}(r/2^d),& r\equiv0\pmod{2^d},\\
0,&\text{otherwise}.
\end{cases}
\]
The reduced target \(r/2^d\) is well-defined as a residue modulo \(2^{n-d}\), including when \(n=d\).

Consequently, the set of sums of two \(d\)-th powers in \(\mathbb Z_2\) is exactly
\[
\mathcal I_t=\{0\}\cup\bigcup_{j\ge0}2^{dj}\left((1+2^h\mathbb Z_2)\cup(2+2^h\mathbb Z_2)\right).
\]
Its additive Haar measure, normalized by \(\mu(\mathbb Z_2)=1\), is
\[
\boxed{\mu(\mathcal I_t)=\frac{2^{d-t-1}}{2^d-1}.}
\]
In particular the measure is \(2/15\) for fourth powers, \(16/255\) for eighth powers, and \(2048/65535\) for sixteenth powers. All these formulas are valid for every indicated exponent and modulus; the inclusion of \(0\) concerns the dyadic image and has measure zero.

## Assumptions and scope

The variables range over complete residue rings, with repetitions and zero permitted. Multiplicity counts **ordered** pairs. A target modulo \(2^n\) is not an integer equality; the Haar image statement concerns actual elements of \(\mathbb Z_2\). There are no primitivity assumptions or restrictions on the valuations of the inputs. The power exponent is \(2^t\) with \(t\ge2\); neither arbitrary exponents nor odd prime-power moduli are asserted.

## Proof

**Unit-power lemma.** For every \(n\ge h\), the map \(u\mapsto u^d\) on the odd residue classes modulo \(2^n\) has image precisely the coset group \(1+2^h\mathbb Z/2^n\mathbb Z\). Every element of that image has exactly \(2^{t+1}\) odd preimages. Indeed, for \(n\ge3\) the unit group is isomorphic to \(C_2\times C_{2^{n-2}}\). Raising to \(2^t\) kills the sign and multiplies the cyclic exponent by \(2^t\). Since \(n\ge t+2\), the kernel has order \(2^{t+1}\), and the image is exactly the subgroup of odd residues congruent to one modulo \(2^{t+2}\). The subgroup characterization follows either from this group decomposition or from the standard \(2\)-adic power-unit filtration.

**Small moduli.** Since \(h\le d\) when \(t\ge2\), for \(n<h\) the \(d\)-th power of every even residue is zero modulo \(2^n\), whereas the \(d\)-th power of every odd residue is one. Count the ordered parity patterns: even/even, mixed parity, and odd/odd contribute \(q^2/4,q^2/2,q^2/4\) for \(n\ge2\). At \(n=1\), the first and last patterns coincide modulo \(2\); direct enumeration gives \(2\) solutions to each target.

**Mixed-parity and odd/odd branches.** Fix \(n\ge h\). Every even \(y\) has \(y^d\equiv0\pmod{2^h}\). For any target \(r\equiv1\pmod{2^h}\), the unit-power lemma gives \(2^{t+1}\) choices of odd \(x\) for each of \(q/2\) even \(y\); two possible orders produce \(2^{t+1}q\) representations. An odd/odd pair must sum to \(2\pmod{2^h}\). Conversely, for \(r\equiv2\pmod{2^h}\), each of \(q/2\) odd \(x\) admits \(2^{t+1}\) odd \(y\); the count is \(2^tq\). These branches are exhaustive unless both inputs are even, because \(h\ge4\) makes the three parity residues \(0,1,2\pmod{2^h}\) distinct.

**Even/even branch.** For \(h\le n<d\), even \(d\)-th powers vanish modulo \(2^n\), so all \(q^2/4\) even/even pairs yield target zero. If \(n\ge d\), write \(x=2u\) and \(y=2v\), where \(u,v\) independently range modulo \(2^{n-1}\). The congruence becomes \(u^d+v^d\equiv r/2^d\pmod{2^{n-d}}\) whenever \(2^d\mid r\); otherwise it is impossible. Every prescribed residue \(u\pmod{2^{n-d}}\) has exactly \(2^{d-1}\) lifts to a residue modulo \(2^{n-1}\), and likewise for \(v\). Hence the exact factor \(2^{2(d-1)}\) and the recursion above. Induction in \(n\) now proves every representation-count formula.

**Full dyadic image.** If a nonzero dyadic target is representable and both inputs are even, divide both by two. Its valuation decreases by exactly \(d\). This process terminates unless the represented target is zero. At its first step with an odd input, the target belongs to \(1+2^h\mathbb Z_2\) or \(2+2^h\mathbb Z_2\). Conversely the unit-power lemma remains valid over \(\mathbb Z_2\) (the inverse limit of the finite unit groups), so every target in either coset is a sum of two powers, using respectively one odd and one even input, or two odd inputs. Scaling both inputs by \(2^j\) gives all displayed valuation layers. Their valuations are exactly \(dj\) or \(dj+1\), so the layers are disjoint. Each of the two cosets at depth \(dj\) has Haar measure \(2^{-dj-h}\); summing the geometric series gives
\[
\mu(\mathcal I_t)=2\sum_{j\ge0}2^{-dj-h}=\frac{2^{1-h}}{1-2^{-d}}=\frac{2^{d-t-1}}{2^d-1}.
\]
This completes the proof.

## Verification

The included standalone Python program `verify.py` computes all \(d\)-th-power residues modulo \(2^n\), forms an independent ordered-pair histogram by cyclic convolution of their multiplicities, and compares **every** target to the closed recursion. It checks \(44\) complete distributions: \(t=2,3\) with \(0\le n\le11\), and \(t=4,5\) with \(0\le n\le9\). Running `python3 verify.py` yields `VERIFIED 44 complete residue distributions`. This is finite corroboration only; the argument for all exponents and moduli is the preceding group-theoretic proof.

## Relationship to prior work

Brüdern and Wooley (first public July 8, 2022) prove a non-singular Hasse principle for **pairs of quartic equations in at least twenty-two variables**. Their discussion of local solutions uses the elementary fact that \(2\)-adic units congruent to one modulo sixteen are fourth powers; it does not formulate a complete two-summand count for each target or the displayed Haar image measure. The old unit-power lemma is used here without claiming novelty. Ramanujam (1963) studies uniform Waring bounds for the number of summands in \(p\)-adic rings; the accessible extract describes a bound of \(8m^5\) powers and does not imply the exact ordered two-summand distribution as stated. Wang’s 1992 diagonal-form Poincaré-series theorem supplies general information about homogeneous zero-target congruence counts, so the zero-target specialization is not claimed separately as novel. The full historical literature may contain equivalent formulas or immediate deductions; these remain a substantive originality risk.

## Limitations

The theorem concerns only powers \(2^t\) with \(t\ge2\) and only dyadic moduli. It does not establish arithmetic representation over the integers, other primes, or a generalized Waring theorem. Counting with the number of terms two and the density of the image of those terms are different invariants. The proof is elementary once the classical structure of dyadic unit groups is known, so possible implicit coverage by older local-congruence work requires continued bibliographic attention. 

## References

1. J. Brüdern and T. D. Wooley, *Pairs Of Diagonal Quartic Forms: The Non-Singular Hasse Principle*, Quarterly Journal of Mathematics 74 (2023), 101–128; first published July 8, 2022, DOI 10.1093/qmath/haac019, https://doi.org/10.1093/qmath/haac019 .
2. C. P. Ramanujam, *Sums of m-th powers in p-adic rings*, Mathematika 10 (1963), 137–146, DOI 10.1112/S002557930000406X, https://doi.org/10.1112/S002557930000406X .
3. J. Wang, *On the Poincaré Series for Diagonal Forms*, Proceedings of the American Mathematical Society 116 (1992), 607–611, DOI 10.2307/2159425, https://doi.org/10.2307/2159425 .

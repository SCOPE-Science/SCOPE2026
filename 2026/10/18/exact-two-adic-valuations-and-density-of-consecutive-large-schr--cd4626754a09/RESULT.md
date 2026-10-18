# Exact two-adic valuations and density of consecutive large Schröder-number differences

## Finding
For the classical *large Schröder numbers* \(S_0=1\) and
\[
S_n=\sum_{k=1}^{n}\frac{2^k}{k}\binom{n-1}{k-1}\binom{n}{k-1}\qquad(n\ge1),
\]
define the positive integer \(D_n=S_{n+1}-S_n\). For **every integer \(n\ge1\)**,
\[
\boxed{\nu_2(D_n)=\begin{cases}
2,&n\text{ odd},\\[2pt]
1+\nu_2(n(n+2)),&n\text{ even}.
\end{cases}}
\]
Consequently, \(\nu_2(D_n)=3\) never occurs: \(\nu_2(D_n)=2\) has natural density \(1/2\), and each value \(j\ge4\) occurs with natural density \(2^{-(j-2)}\). More precisely, for every \(j\ge4\), the indices of valuation exactly \(j\) comprise the **two residue classes modulo \(2^{j-1}\)**
\[
n\equiv 2^{j-2}\quad\text{or}\quad n\equiv 2^{j-2}-2\pmod{2^{j-1}}.
\]

The structural reason is a pair of explicit zeros of a continuous two-adic interpolation of the positive-index Schröder numbers. The normalized forward difference is a scaled isometry on each of the two even congruence classes modulo four.

## Assumptions and scope
For an integer \(m\ne0\), \(\nu_2(m)\) is its exact exponent of two. All two-adic congruences and continuity are in \(\mathbb Z_2\). The interpolation constructed below agrees with the combinatorial sequence at **positive indices only**. Its value at \(0\) is \(2\), not the customary initial value \(S_0=1\). The theorem therefore explicitly begins at \(n=1\), and it makes no claim about \(D_0=S_1-S_0=1\).

The only external mathematical input is the proved shift congruence in Theorem 2 of Cao and Pan (2015): for every integer \(n\ge1\) and \(\alpha\ge2\),
\[
S_{n+2^\alpha}-S_n\equiv
(-1)^{\lfloor(n-1)/2\rfloor}2^{\alpha+1}
\pmod{2^{\alpha+3}},
\]
and at \(\alpha=1\), \(S_{n+2}-S_n\equiv4\pmod{16}\).

## Proof
**1. A convergent two-adic interpolation.** Define
\[
\mathcal S(x)=\sum_{k=1}^{\infty}
\frac{2^k}{k}\binom{x-1}{k-1}\binom{x}{k-1},\qquad x\in\mathbb Z_2.
\]
For each \(k\), both binomial polynomials take values in \(\mathbb Z_2\); their product multiplied by \(2^k/k\) has valuation at least \(k-\nu_2(k)\), tending to infinity uniformly in \(x\). Therefore the series converges uniformly and defines a continuous function. When \(n\ge1\) is an ordinary integer, all terms with \(k>n\) vanish and \(\mathcal S(n)=S_n\). Put \(\mathcal D(x)=\mathcal S(x+1)-\mathcal S(x)\), also continuous.

**2. Two exact zeros.** For \(x=0\) and \(x=1\), direct binomial evaluation yields \(\mathcal S(0)=\mathcal S(1)=2\), hence \(\mathcal D(0)=0\). For every \(k\ge1\),
\[
\binom{-2}{k-1}\binom{-1}{k-1}=k,
\quad
\binom{-3}{k-1}\binom{-2}{k-1}=k\binom{k+1}{2}.
\]
Thus, using convergent geometric-power series in \(\mathbb Z_2\),
\[
\mathcal S(-1)=\sum_{k\ge1}2^k=\frac2{1-2}=-2,
\quad
\mathcal S(-2)=\sum_{k\ge1}2^k\binom{k+1}{2}
=\frac2{(1-2)^3}=-2.
\]
Therefore **\(\mathcal D(-2)=0\)** as well.

**3. Local scaled isometry.** Fix \(\alpha\ge2\). The preceding Cao–Pan congruence is a congruence between continuous functions of the integer \(n\), and its sign is constant on each residue class modulo four. Since positive integers are dense in \(\mathbb Z_2\), it extends to every \(x\in\mathbb Z_2\), with the sign interpreted by the residue of \(x\) modulo four. Apply the extended congruence at \(x+1\) and subtract that at \(x\), for any even \(x\in\mathbb Z_2\). The two signs are opposites, giving
\[
\mathcal D(x+2^\alpha)-\mathcal D(x)
\equiv (-1)^{x/2}2^{\alpha+2}\pmod{2^{\alpha+3}}.
\tag{1}
\]
Here \((-1)^{x/2}\) is determined by the parity of \(x/2\), so is a valid sign on even two-adic integers. Repeating (1) an odd number \(u\) of times preserves that sign, because \(\alpha\ge2\). Hence whenever \(x\) is even, \(u\ge1\) is odd, and \(\alpha\ge2\),
\[
\nu_2\bigl(\mathcal D(x+u2^\alpha)-\mathcal D(x)\bigr)=\alpha+2.
\tag{2}
\]
In particular the restriction of \(\mathcal D\) to either class \(0+4\mathbb Z_2\) or \(2+4\mathbb Z_2\) is a distance-scaled two-adic isometry (by a factor with valuation two); the statement for general two-adic pairs follows by density from (2).

**4. Exact integer valuations.** If \(n\ge4\) and \(n\equiv0\pmod4\), let \(\alpha=\nu_2(n)\ge2\) and take \(x=0\), \(u=n/2^\alpha\) in (2). Because \(\mathcal D(0)=0\) and \(\mathcal D(n)=D_n\), this gives \(\nu_2(D_n)=\nu_2(n)+2\). Here \(\nu_2(n+2)=1\), so the result equals \(1+\nu_2(n(n+2))\).

If \(n\ge2\) and \(n\equiv2\pmod4\), set \(\alpha=\nu_2(n+2)\ge2\), \(x=-2\), and \(u=(n+2)/2^\alpha\), an odd positive integer. Now (2) and \(\mathcal D(-2)=0\) give \(\nu_2(D_n)=\nu_2(n+2)+2=1+\nu_2(n(n+2))\), because \(\nu_2(n)=1\).

For odd \(n\ge1\), subtract the two congruences \(S_{m+2}-S_m\equiv4\pmod{16}\) at consecutive positive indices \(m=n,n+1\). This yields \(D_{n+2}-D_n\equiv0\pmod{16}\). Since \(D_1=S_2-S_1=4\), all odd \(n\ge1\) satisfy \(D_n\equiv4\pmod{16}\), completing the valuation formula.

**5. Natural densities.** For even \(n\), the proof yields \(\nu_2(D_n)=\nu_2(n)+2\) when \(n\equiv0\pmod4\), and \(\nu_2(D_n)=\nu_2(n+2)+2\) when \(n\equiv2\pmod4\). The exact-level condition \(\nu_2(D_n)=j\) for \(j\ge4\) therefore specifies exactly the two residue classes displayed in the Finding section modulo \(2^{j-1}\), each of natural density \(2^{-(j-1)}\). Odd indices have natural density \(1/2\) and valuation two. No other valuation occurs.

## Verification
The self-contained Python program `VERIFY.py` regenerates the first 2,049 classical large Schröder numbers via the exact integral three-term recurrence; it checks the claimed valuations for positive indices through 2,030, verifies both congruences supplied by Cao–Pan over a finite test rectangle, checks the derived finite-level residue classes and selected two-adic series evaluations modulo large powers of two. It prints `VERIFY_OK` on success. Run with `python3 VERIFY.py` in a directory containing that file. These computations are independent finite consistency checks, not replacements for the proof for all positive integers.

## Relationship to prior work
Cao and Pan, *A Stern-type congruence for the Schroder numbers* (arXiv:1512.06310v1, publicly posted 20 December 2015), prove the pointwise shift congruences above, including the sharper modulus used in (1). Their Theorem 2, rather than its weaker abstract-level version, is the essential input here. Their paper also supplies the Narayana expansion used to define \(\mathcal S\). This work does **not** claim either of those ingredients as new. The new mathematical assertions concern the evaluation of the two zero locations \(0,-2\) of the interpolated forward difference and the resulting complete exact valuation law and natural-density classification. The published shift statement itself does not supply the zero locations or the resulting valuation levels.

The OEIS record A006318 and standard Schröder-number references describe the underlying sequence and recurrences. A 2024 paper by Jia and Huang on congruences involving Delannoy and little Schröder numbers focuses on weighted sums, rather than these consecutive-index valuation fibres. Direct literature and mathematical research-record searches located no equivalent evaluated formula, but negative search results are not a proof of universal novelty.

## Limitations
The theorem concerns the large Schröder numbers at positive indices and the exact two-adic valuation of their first differences; it does not assert any odd-prime analogue. The interpolation's value at zero is 2 and must not be substituted for the separate combinatorial convention \(S_0=1\). The proof depends on Cao–Pan's previously proved Theorem 2; it is not an independent new proof of that theorem. Novelty is subject to the risk of an unindexed earlier derivation or a more general unstated equivalent result. Independent audit has not been performed.

## References
1. Hui-Qin Cao and Hao Pan, *A Stern-type congruence for the Schroder numbers*, arXiv:1512.06310v1 (20 December 2015), Theorem 2 and equation (7), https://arxiv.org/pdf/1512.06310.
2. OEIS Foundation, *A006318: Large Schröder numbers*, https://oeis.org/A006318.
3. Chen-Bo Jia and Jia-Qing Huang, *Congruences involving Delannoy numbers and Schröder numbers*, arXiv:2410.17522 (23 October 2024), for comparison of related weighted-sum questions, https://arxiv.org/abs/2410.17522.

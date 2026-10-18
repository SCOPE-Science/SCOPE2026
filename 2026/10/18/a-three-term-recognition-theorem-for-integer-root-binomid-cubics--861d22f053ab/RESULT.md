# A three-term recognition theorem for integer-root binomid cubics

## Finding

For integers \(0\le a\le b\le c\), set
\[
 f_n=(n+a)(n+b)(n+c)\qquad(n\ge1).
\]
For every integer \(n\ge0\) and \(0\le k\le n\), define the generalized binomial coefficient
\[
 \left[\!\begin{matrix}n\\k\end{matrix}\!\right]_f
 =\frac{f_n f_{n-1}\cdots f_{n-k+1}}{f_kf_{k-1}\cdots f_1},
\]
where an empty product is \(1\). A sequence is *binomid* when all these quotients are integers.

**Theorem.** In the family above, the following are equivalent:

1. \(f\) is binomid.
2. Both \(f_2/f_1\) and \(f_3/f_1\) are integers.
3. \((a,b,c)\) is one of \((0,0,0)\), \((0,0,1)\), or \((0,1,2)\).

Thus two divisibility tests on the first three terms decide an infinite set of generalized binomial-coefficient constraints for *every* cubic polynomial whose three roots, with multiplicity, are nonpositive integers. The result also holds after multiplication by any nonzero constant that keeps the sequence integer-valued: the constant cancels from every generalized binomial coefficient.

## Assumptions and scope

The parameters \(a,b,c\) are integers, sorted without loss of generality, and nonnegative. The sequence begins at \(n=1\); its terms are strictly positive. Binomid means integral for **every** \(n\ge0\) and \(0\le k\le n\), not just a bounded computation. The theorem does not classify general integer-valued cubic polynomials with nonintegral, positive, or nonreal roots.

## Proof

**Necessity and finite reduction.** If \(f\) is binomid, choosing \(k=1\) and \(n=2,3\) forces \(f_1\mid f_2\) and \(f_1\mid f_3\). Put
\[
 u_t=\frac{t+2}{t+1}=1+\frac1{t+1},\qquad
 R=\frac{f_2}{f_1}=u_a u_bu_c.
\]
The function \(u_t\) strictly decreases with nonnegative integer \(t\), and \(u_t>1\). We classify **all** ordered triples for which \(R\) is an integer.

If \(a\ge3\), then \(1<R\le(5/4)^3=125/64<2\), impossible. Thus \(a\le2\). For each remaining value, the following monotone bounds force a finite range for \(b\):
\[
\begin{array}{c|c|c}
 a & \text{excluded range for }b & \text{upper bound for }R\\\hline
 0 & b\ge4 & 2(6/5)^2=72/25<3\\
 1 & b\ge6 & (3/2)(8/7)^2=96/49<2\\
 2 & b\ge4 & (4/3)(6/5)^2=48/25<2.
\end{array}
\]
In the first row \(R>2\), and in the remaining rows \(R>1\), so no integer lies in the respective intervals. In all cases \(a\le b\le c\).

For each of these finitely many \((a,b)\), put \(K=u_a u_b\). An integer \(m=R\) must satisfy
\[
 K<m\le K u_b,
 \qquad c+1=\frac{K}{m-K}.
\]
Indeed, \(u_c>1\) and \(u_c\le u_b\). Conversely, a proposed integer \(m\) in that interval gives a valid \(c\) exactly when \(K/(m-K)\) is an integer at least \(b+1\). Evaluating these exact fractions gives *precisely* the following twelve triples; the final column is \(f_3/f_1\), included to perform the second necessary divisibility test:

| \((a,b,c)\) | \(f_2/f_1\) | \(f_3/f_1\) |
|---|---:|---:|
| \((0,0,0)\) | \(8\) | \(27\) |
| \((0,0,1)\) | \(6\) | \(18\) |
| \((0,0,3)\) | \(5\) | \(27/2\) |
| \((0,1,2)\) | \(4\) | \(10\) |
| \((0,2,7)\) | \(3\) | \(25/4\) |
| \((0,3,4)\) | \(3\) | \(63/10\) |
| \((1,1,2)\) | \(3\) | \(20/3\) |
| \((1,3,14)\) | \(2\) | \(17/5\) |
| \((1,4,8)\) | \(2\) | \(154/45\) |
| \((1,5,6)\) | \(2\) | \(24/7\) |
| \((2,2,7)\) | \(2\) | \(125/36\) |
| \((2,3,4)\) | \(2\) | \(7/2\) |

Only the three triples asserted in the theorem survive both tests. This establishes implication (2) to (3), while (1) to (2) was immediate.

**Sufficiency.** We recall the established binomid properties of \(I_n=n\) and the Pascal-column sequences \(C_m(n)=\binom{n+m-1}{m}\). The Pascal-column property has the independent integer-determinant identity
\[
 \left[\!\begin{matrix}N\\k\end{matrix}\!\right]_{C_m}
 =\det\!\left[\binom{N-k+m+i}{m+j}\right]_{0\le i,j<k}
 \quad(N\ge k\ge1),
\]
recorded by Shapiro (2023), §1, with earlier attribution to Netto and von Zeipel. The right-hand side is an integer because all matrix entries are ordinary binomial coefficients of nonnegative integral arguments. Thus \(C_2\) and \(C_3\) are binomid. Also, if \(g\) and \(h\) are binomid, then their termwise product is binomid, because the associated generalized binomial coefficients multiply. Multiplying a sequence by a nonzero constant does not change any quotient.

For the three surviving triples the corresponding sequences are
\[
 n^3=I_n^3,\qquad
 n^2(n+1)=2I_n C_2(n),\qquad
 n(n+1)(n+2)=6C_3(n).
\]
Each is binomid by the preceding facts. Hence (3) implies (1), completing all equivalences. \(\square\)

## Verification

Run `python3 verify.py` in the directory containing the companion script. The script enumerates the twelve candidates **without truncating \(c\)**, using the exact rational equation \(c+1=K/(m-K)\); it checks both necessary fractions and the three surviving triples. It independently verifies \(15{,}450\) generalized binomial coefficients for \(n\le100\), \(350\) Pascal-column determinant identities for \(m=2,3\), and the finite sanity scan of \(45{,}100\) ordered triples in a stated box. The output is provided in `verification_output.txt`. The unrestricted proof is the monotonic bound, exact candidate equation, and integral determinant argument; finite checks alone would not establish the theorem.

## Relationship to prior work

Shapiro's *Divisibility Properties for Integer Sequences* (arXiv first public version 4 February 2023; published in *Integers* 23 (2023), Article A57) defines binomid sequences and proves product closure and integrality for Pascal columns. Those published results cover the sufficiency of the three survivors. The journal version's Theorem 26 classifies all binomid polynomials of degree at most two and Open Problem 27 asks for the degree-three classification. Neither the lower-degree classification nor known individual positive examples excludes further integer-root cubic examples. This theorem supplies a full classification of the natural **nonpositive integer-root** cubic subclass, together with a finite three-term recognition criterion; it does not solve the unrestricted open problem.

Caalim and Tanaka (2024) study binomid indices and their lexicographically minimal extensions, giving a valuation-based framework and periodicity results. Their characterization can restate generalized-binomial integrality prime by prime, but the inspected results do not classify cubic polynomials by their three root shifts or give the finite coefficient test above.

## Limitations

Only cubic polynomials splitting completely as three linear factors with nonpositive integer roots (up to a nonzero scalar) are covered. This does not classify cubics with rational nonintegral roots, irreducible factors, or roots outside the stated half-line; nor does it establish binomid integrality at every level of the binomid pyramid. The proof uses previously established Pascal-column integrality. An equivalent classification in literature not recovered by the cited searches remains possible.

## References

1. Daniel B. Shapiro, *Divisibility Properties for Integer Sequences*, arXiv:2302.02243v1 (first public 2023-02-04); *Integers* **23** (2023), Article A57, DOI 10.5281/zenodo.8214835. Open preprint: https://arxiv.org/html/2302.02243v1; published version: https://math.colgate.edu/~integers/x57/x57.pdf.
2. Jonathan Caalim and Yu-ichi Tanaka, *Lexicographically Minimal Extension of a Finite Binomid Index*, *Integers* **24** (2024), Article A53, DOI 10.5281/zenodo.11221709. https://math.colgate.edu/~integers/y53/y53.pdf.
3. D. B. Shapiro (2023), §1, citing E. Netto, *Lehrbuch der Combinatorik* (1901), p. 257, for the binomial determinant identity used here; earlier attribution to von Zeipel (1865).

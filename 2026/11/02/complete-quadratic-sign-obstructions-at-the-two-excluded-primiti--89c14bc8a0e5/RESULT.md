# Complete quadratic sign obstructions at the two excluded primitive-root primes

## Finding
For \(p\in\{19,31\}\), let \(G_p\) be the set of primitive roots in \(\mathbb F_p^\times\), and let \(\chi_p\) be the quadratic character, with \(\chi_p(0)=0\). Consider triples \((a,b,c)\in\mathbb F_p^3\setminus\{0\}\) such that \((a,c)\ne(0,0)\) and \(b^2-4ac\ne0\). Declare a triple *sign-obstructed* if the values \(\{\chi_p(ag^2+bg+c):g\in G_p\}\) do not contain both \(+1\) and \(-1\). This property is invariant under multiplying the triple by any nonzero field element. Each projective triple has a unique representative whose first nonzero coefficient (in the order \(a,b,c\)) equals \(1\).

For \(p=19\), the sign-obstructed projective triples are **exactly nine**:

\[
(1,1,7),\ (1,2,7),\ (1,2,11),\ (1,3,1),\ (1,3,11),\
(1,7,1),\ (1,11,11),\ (1,14,1),\ (1,14,7).
\]

For \(p=31\), they are **exactly three**:

\[
(1,6,1),\ (1,7,12),\ (1,29,13).
\]

The admissible projective-class totals are respectively \(360\) and \(960\). Thus the fractions of admissible classes that fail the two-sign property are exactly \(1/40\) and \(1/320\), respectively. Equivalently, exactly \(162\) admissible raw coefficient triples fail modulo \(19\), and exactly \(90\) fail modulo \(31\).

## Assumptions and scope
The result concerns the two explicitly excluded primes in a quadratic-character existence question. A zero polynomial value is neither a nonzero square nor a nonsquare, so zeros are ignored when deciding whether both signs occur. Triples with zero discriminant, or \(a=c=0\), are excluded. All coefficients, discriminants and polynomial values are reduced in \(\mathbb F_p\). No other primes are claimed.

## Proof
Every nonzero coefficient triple belongs to a unique projective class under nonzero scalar multiplication. Multiplication of all values by a square preserves signs, and multiplication by a nonsquare exchanges the two signs; either action preserves the property of *not containing both signs*. Normalize by the first nonzero coefficient. There are precisely \(p^2+p+1\) normalized projective triples: \((1,b,c)\) for all \(b,c\), \((0,1,c)\) for all \(c\), and \((0,0,1)\). The discriminant-zero equation defines a nondegenerate projective conic with \(p+1\) points; the additional forbidden projective class \((0,1,0)\) has nonzero discriminant. Therefore exactly \(p^2-1\) classes are admissible.

Here is an exhaustive integer-arithmetic certificate of the exceptional classes. For each of the two specified primes, factor \(p-1\) into its distinct prime divisors \(r\). An integer \(g\in\{1,\ldots,p-1\}\) is a primitive root if and only if \(g^{(p-1)/r}\not\equiv1\pmod p\) for every such \(r\). This yields

\[
G_{19}=\{2,3,10,13,14,15\},\qquad
G_{31}=\{3,11,12,13,17,21,22,24\}.
\]

Compute the set of nonzero square residues \(R_p=\{x^2\bmod p:1\le x<p\}\). Enumerate **every** normalized triple from the preceding three disjoint families. Discard precisely those failing either admissibility test. For every remaining triple evaluate \(z_g=(ag^2+bg+c)\bmod p\) for every \(g\in G_p\). Set the positive indicator if any \(z_g\in R_p\), and the negative indicator if any \(z_g\ne0\) is outside \(R_p\). Keep the triple exactly when one of these indicators is false. The full executable implementation is the standalone `verify.py` included with this result; its `run()` routine executes these finite loops literally and compares the entire sorted output, not merely its cardinality, with the displayed tables.

For an independent exhaustive check of normalization and the projective quotient, the same certificate also loops over **all** \(p^3\) raw triples, applies the original sign predicate without normalization, and normalizes only at the end. The resulting sets coincide exactly with the primary enumeration, and the number of raw exceptions equals \((p-1)\) times each table length. All loops have explicit finite bounds with integer modular arithmetic and no heuristic stopping. This constitutes an exhaustive finite proof at the two specified primes, rather than an inference from a finite experiment about other primes. The admissible projective counts are \(19^2-1=360\) and \(31^2-1=960\); raw exceptional counts are \(9(19-1)=162\) and \(3(31-1)=90\).

## Verification
Run `python3 verify.py` with standard Python 3. The script checks the complete displayed tables, the primitive-root lists, the admissible counts and the two independent enumeration schemes. It requires no outside data or packages. The checked output reports \(9\) exceptional classes for \(19\) and \(3\) for \(31\); no probabilistic sampling or numerical approximations are used.

## Relationship to prior work
Sun's preprint *New observations on primitive roots modulo primes* had a publicly accessible fourth version on 2014-05-29 discussing Han's 1989 work on the values of quadratic polynomials at primitive roots. The later fifth version, dated 2020-02-28, explicitly states Conjecture 4.9 and excludes the primes \(19\) and \(31\) from its two-sign conclusion (printed p.16). The complete projective coefficient tables above are not supplied by either inspected version. The present theorem resolves only the **exact structure of those two excluded finite cases**, not the conjecture for other primes. In particular, the dated conjecture statement in the later version should not be mistaken for material already verified as present in the fourth version.

## Limitations
The table is an exact, computer-checkable exhaustive classification for precisely two small primes, with source code forming an essential part of its finite proof. It does not establish a uniform theorem for other primes. Other mathematical literature might have previously tabulated or implied the same small-prime classification; no independent literature audit has been performed.

## References
Z.-W. Sun, *New observations on primitive roots modulo primes*, arXiv:1405.0290v4 (public revision 2014-05-29), pp.1–2, discussion of W. B. Han's polynomial/primitive-root results, https://arxiv.org/pdf/1405.0290v4 .

Z.-W. Sun, *New observations on primitive roots modulo primes*, arXiv:1405.0290v5 (revision 2020-02-28), p.16, Conjecture 4.9 and its exceptional primes, https://arxiv.org/pdf/1405.0290v5 .

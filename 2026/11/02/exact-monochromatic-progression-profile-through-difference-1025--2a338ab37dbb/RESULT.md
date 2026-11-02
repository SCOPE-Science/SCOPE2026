# Exact monochromatic-progression profile through difference 1025 in the 0011/1100 fixed point

## Finding

Let \(t\) be the one-sided fixed point beginning in \(0\) of the substitution \(0\mapsto0011\), \(1\mapsto1100\). For an integer \(d\ge1\), let \(A(d)\) be the largest \(L\) for which there exists an integer \(i\ge0\) with \(t_i=t_{i+d}=\cdots=t_{i+(L-1)d}\). The complete, exact values of \(A(d)\), for every \(1\le d\le1025\), are the 1025 records of `AP_PROFILE.csv`. Every record also supplies a starting-position witness.

Among the full ranges of eligible differences, the three successive natural substitution scales have *unique* maximizers:

| All differences searched | Exact maximum | Unique maximizing difference | Second-highest value |
|:--|--:|--:|--:|
| \(1\le d\le65\) | 66 | 65 | 64 |
| \(1\le d\le257\) | 260 | 255 | 258 |
| \(1\le d\le1025\) | 1026 | 1025 | 1024 |

Thus the first three nontrivial scales \(n=3,4,5\) in Conjecture 30 of Aedo–Grimm–Nagai–Staynova have the conjectured maximum and a uniquely maximizing difference for this particular fixed point. The theorem is a *finite difference bound with infinite starting positions*, not a claim about larger difference cutoffs.

## Assumptions and scope

All indices are zero based. The fixed point has the exact base-four digit formula
\[
t_m=\bigoplus_{j\ge0}\left\lfloor\frac{(\lfloor m/4^j\rfloor\bmod4)}{2}\right\rfloor,\qquad m\ge0.
\]
Here \(\oplus\) is binary addition modulo two. For every \(B=4^k\), every \(m\ge0\), and every \(0\le r<B\), one has \(t_{Bm+r}=t_m\oplus t_r\). Our finite-bound computation uses \(1\le d\le1025\), and tests all lengths up to 1032, for every possible infinite-word starting position.

## Proof

**One-carry reduction.** Fix a difference \(d\) and a candidate length \(L\) and select \(B=4^k>(L-1)d\). Any starting position has a unique representation \(i=Bm+r\) with \(0\le r<B\). For \(0\le j<L\), put
\[
c_j=\left\lfloor\frac{r+jd}{B}\right\rfloor\in\{0,1\},\qquad u_j=(r+jd)\bmod B.
\]
The digit identity gives \(t_{i+jd}=t_{m+c_j}\oplus t_{u_j}\). The sequence of carries \(c_j\) is nondecreasing. Consequently, existence of a monochromatic length-\(L\) progression is equivalent to existence of a residue \(r\) for which the low-digit bits \(t_{u_j}\) are constant separately before and after the unique possible carry transition. In the forward direction this follows because the high digit term is fixed within each carry group. Conversely, if the low-digit colors in the groups are \(a,b\), take \(m=0\) when \(a=b\), since \(t_0=t_1=0\); take \(m=1\) when \(a\ne b\), since \(t_1=0,t_2=1\). When there is no carry, \(m=0\) suffices. This establishes an *if and only if* reduction over all unbounded starting positions.

**Exact bit-vector exhaustion.** Set \(L_{\max}=1032\) and, for each \(d\), select the least \(B=4^k>1031d\). Encode the \(B\) low-digit colors as the integer bit-vector \(T=\sum_{r=0}^{B-1}t_r2^r\). Its base-four recursion from \(T=0,B=1\) is the four concatenated blocks \(T,T,\overline T,\overline T\). At transition \(j-1\) to \(j\), shift-rotate \(T\) by \(jd\), compare it to the rotation by \((j-1)d\), and permit a difference only at the unique boundary residue for which the carry changes. Intersect the resulting compatibility masks for all \(j=1,\ldots,L-1\). Because every residue is represented by one bit, this is an exhaustive finite test of exactly the equivalent condition above, not an empirical scan over an initial prefix.

The companion `verify.py` implements the explicit operations using arbitrary-precision integers. At each \(d\), a nonzero survivor mask establishes a length-\(L\) witness, and its first zero mask proves the impossibility of length \(L+1\) or longer. The certificate never reaches the 1032-length cap. The output is exactly the table `AP_PROFILE.csv`, including the explicit infinite-word starting-position witnesses. Taking ordinary maxima of these 1025 proved values gives the three strict unique-maximizer rows above.

## Verification

Run `python3 verify.py` in a directory containing `verify.py` and `AP_PROFILE.csv`. It recomputes all \(A(d)\) from the substitution, checks all 1025 file records, checks each witness directly using the base-four digit formula, and checks the three maxima and uniqueness. It requires only Python 3's standard library and prints `VERIFY_OK` on success. A separate direct prefix-state enumeration and a vectorized residue implementation were also compared in the investigation, but are not needed to reproduce the certificate.

## Relationship to prior work

Aedo, Grimm, Nagai and Staynova [1] introduce exactly the binary Morse-like family and its maximum arithmetic-progression-length invariant. Their Conjecture 30 predicts maxima at substitution-scale cutoffs and establishes particular long progressions at differences one above or below powers of four. Those individual endpoint witnesses do not imply that no *other* smaller differences have longer progressions. The present result performs that missing all-differences comparison for three natural finite scales and records the complete 1025-value profile.

Aedo, Grimm, Mañibo, Nagai and Staynova [2] derive group-based growth estimates for related automatic sequences; the inspected results do not give the complete exact profile here. The result does not claim a proof of [1, Conjecture 30] for all scales.

## Limitations

No assertion is made for \(d>1025\), for arbitrary substitution parameters, or for the validity of Conjecture 30 at every scale. The bit-vector certificate is an exhaustive finite proof that depends on the stated reduction lemma; it is not a general closed-form expression for \(A(d)\). Independent scientific evaluation has not been performed.

## References

[1] I. Aedo, U. Grimm, Y. Nagai and P. Staynova, *On long arithmetic progressions in binary Morse-like words*, arXiv:2101.02056, first public 2021-01-06; specifically the generalized binary Thue–Morse definition, Propositions 27–28 and Conjecture 30. https://arxiv.org/abs/2101.02056

[2] I. Aedo, U. Grimm, N. Mañibo, Y. Nagai and P. Staynova, *Monochromatic arithmetic progressions in automatic sequences with group structure*, arXiv:2302.12908, first public 2023-02-24. https://arxiv.org/abs/2302.12908

# Exact Fibonacci state-cycle census modulo powers of five

## Finding

For every integer \(k\ge 1\), write \(R_k=\mathbb Z/5^k\mathbb Z\) and let \(T_k:R_k^2\to R_k^2\) be the Fibonacci recurrence permutation \(T_k(a,b)=(b,a+b)\). Its complete cycle-length census is:

\[
 c_d(k)=\begin{cases}
 1,&d=1,\\
 1,&d=4,\\
 6\cdot 5^{j-1},&d=4\cdot 5^j,\quad 1\le j<k,\\
 5^{k-1},&d=4\cdot 5^k,\\
 0,&\text{otherwise}.
 \end{cases}
\]

Consequently the total number of distinct cycles is exactly
\[
 \sum_{d\ge1}c_d(k)=\frac{5^k+1}{2}.
\]
For \(k=0\), the one-element state space modulo \(1\) consists of one fixed point, and the same total formula holds. Thus the formula conjectured for the powers-of-five subsequence of OEIS A015134 holds at every exponent, with the stronger full histogram above.

## Assumptions and scope

A *state* is an ordered pair \((a,b)\in R_k^2\); a *cycle* is one orbit under \(T_k\), not one period represented by each of its states. Distinct cyclic shifts of a state are counted as a single cycle. Since the matrix \(Q=\left(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\right)\) has determinant \(-1\), it acts bijectively on \(R_k^2\), so there are no transient states. All exponents \(k\ge1\) are included, without restrictions on the seed pair.

## Proof

**Step 1: the lifting matrix.** Set \(B=Q^4-I=\left(\begin{smallmatrix}1&3\\3&4\end{smallmatrix}\right)\). Direct multiplication gives \(B^2=5(B+I)\) and \(\det B=-5\). Define integral matrices \(C_j\) by
\[
 Q^{4\cdot5^j}=I+5^j C_j,\qquad j\ge0.
\]
Here \(C_0=B\). Raising the identity for \(j\) to the fifth power shows inductively that \(C_{j+1}\) is integral, with
\[
 C_{j+1}-C_j=2\cdot5^j C_j^2+2\cdot5^{2j} C_j^3+5^{3j} C_j^4+5^{4j-1}C_j^5.
\]
(The last displayed exponent is nonnegative for every \(j\ge1\); the first step is treated directly.) Exact calculation gives
\[
 C_1=\frac{Q^{20}-I}{5}
 =\begin{pmatrix}836&1353\\1353&2189\end{pmatrix},\qquad
 C_1\equiv B\pmod5,\quad \det C_1=-605=-5\cdot 121.
\]
For \(j\ge1\), assume \(C_j\equiv B\pmod5\). Since \(B^2\equiv0\pmod5\), also \(C_j^2\equiv0\pmod5\). Each term of the displayed difference is then divisible by \(25\). Consequently \(C_{j+1}\equiv C_j\pmod{25}\), proving \(C_j\equiv C_1\pmod{25}\) for every \(j\ge1\). Thus for every \(j\ge0\), some entry of \(C_j\) is a unit modulo \(5\), while \(\nu_5(\det C_j)=1\). Indeed this follows from the explicit \(C_0\) and \(C_1\), and for \(j\ge1\) from congruence modulo \(25\).

**Step 2: exact fixed-point counts.** The two Smith invariant factors of \(C_j\) over the \(5\)-adic integers have valuations \(0\) and \(1\), because an entry is a unit and its determinant has valuation \(1\). Hence the two Smith valuations of \(Q^{4\cdot5^j}-I=5^jC_j\) are \(j\) and \(j+1\). On \(R_k^2\) the number of vectors fixed by the \(4\cdot5^j\)-th iterate is therefore
\[
 f_j(k):=|\ker(Q^{4\cdot5^j}-I\pmod{5^k})|
 =5^{\min(j,k)+\min(j+1,k)}.\tag{1}
\]
In particular \(f_k(k)=5^{2k}\), so every state has period dividing \(4\cdot5^k\).

**Step 3: possible positive periods.** Modulo \(5\), the characteristic polynomial of \(Q\) is \((X-3)^2\). Because \(3\in\mathbb F_5^\times\) has order \(4\), for any positive \(t\) not divisible by \(4\), the matrix \(Q^t-I\) is invertible modulo \(5\) and hence modulo \(5^k\). Thus no nonzero state has such a period. The only possible exact periods of nonzero states are \(4\cdot5^j\) for \(0\le j\le k\); the zero state is the sole fixed point. The period-divisibility statement from Step 2 excludes all other possibilities.

**Step 4: subtract fixed-point sets.** By (1), \(f_0(k)=5\), hence there are \(5-1=4\) nonzero states of exact period \(4\), forming one cycle. For each \(1\le j<k\), equation (1) yields exactly
\[
 f_j(k)-f_{j-1}(k)=5^{2j+1}-5^{2j-1}=24\cdot5^{2j-1}
\]
new states of exact period \(4\cdot5^j\), hence \(6\cdot5^{j-1}\) such cycles. At the final depth, the number of states of exact period \(4\cdot5^k\) is
\[
 f_k(k)-f_{k-1}(k)=5^{2k}-5^{2k-1}=4\cdot5^{2k-1},
\]
which gives \(5^{k-1}\) cycles. Together with the sole zero-state fixed point, this proves the census, including \(k=1\). Summing the counts gives \(2+\sum_{j=1}^{k-1}6\cdot5^{j-1}+5^{k-1}=(5^k+1)/2\). \(\square\)

## Verification

Run the provided pure-Python file `verify.py` using `python3 verify.py`. It enumerates every state and actual cycle for \(k=1,2,3,4\), totaling \(406900\) states; it separately counts fixed points for \(14\) matrix-exponent/modulus pairs and checks nine lifted matrices through \(j=8\). Expected output is `VERIFY_OK: 406900 enumerated states; 14 fixed-point checks; 9 lift checks`. These finite tests corroborate but do not replace the uniform Smith-valuation proof.

## Relationship to prior work

The published OEIS entry A015134 defines precisely the number of distinct Fibonacci recurrence cycles and explicitly labels \(a(5^n)=(5^n+1)/2\) a conjecture (Stephen Bartell, 20 August 2023). The present proof establishes that formula and specifies every exact cycle length and multiplicity. Coleman--Dugan--McEwen--Reiter--Tang (2006), especially Proposition 4 and Theorem 7, analyze generalized initial conditions and provide a general class equation for cycle counts, but the inspected statements do not supply the needed \(5\)-adic Smith valuations or this complete prime-power census. Their class equation is compatible with, but alone does not imply, the claimed histogram. The case \(k=1\) and the existence of the unique four-cycle are consistent with their known special results.

## Limitations

The theorem concerns the Fibonacci state permutation over moduli that are *pure powers of five*. It does not classify cycles for other prime powers or composite products, nor does it assert a novel general class equation. Finite verification is not an independent proof. The literature comparison is based on identified and materially inspected sources and can be superseded by an unlocated stronger theorem.

## References

1. OEIS, **A015134**, Fibonacci-type sequences modulo an integer, https://oeis.org/A015134. The dated 20 November 2003 comment documents the archival entry; the power-of-five conjecture was added 20 August 2023.
2. D. A. Coleman, C. J. Dugan, R. A. McEwen, C. A. Reiter, T. T. Tang, *Periods of (q,r)-Fibonacci Sequences and Elliptic Curves*, *Fibonacci Quarterly* 44 (2006), 59–70, author-available preprint: https://webbox.lafayette.edu/~reiterc/nt/qr_fib_ec_preprint.pdf.

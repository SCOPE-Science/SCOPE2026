# Complete residue moduli and local isometries for the split-root Jacobsthal family

## Finding

Let \(a\ge2\) be **even** and let \(J_n^{(a)}\) be the integer sequence given by
\[
J_0^{(a)}=0,\quad J_1^{(a)}=1,\quad J_{n+2}^{(a)}=(a-1)J_{n+1}^{(a)}+aJ_n^{(a)}.
\]
It has the closed form
\[
J_n^{(a)}=\frac{a^n-(-1)^n}{a+1}.
\]
Write \(\mathcal C(a)\) for the set of positive integers \(m\) such that for each residue \(r\pmod m\) there is an \(n\ge0\) with \(J_n^{(a)}\equiv r\pmod m\). The exact classification is
\[
\boxed{\mathcal C(a)=\{1,2\}\cup\bigl(\{3\}\text{ if }3\mid a\bigr)\cup\{m\ge1:m\text{ odd},\ p\mid m\Longrightarrow p\mid a+1\}.}
\]
The conditional set \(\{3\}\) is empty unless \(3\mid a\). In the final set, for every \(m\), **both** the even- and odd-indexed subsequences give exact permutations of residues modulo \(m\) over their first \(m\) terms. In particular, the first \(2m\) terms contain each residue exactly twice.

For every odd prime \(p\mid a+1\), the stronger local identity holds for all distinct nonnegative integers \(i,j\):
\[
\boxed{v_p(J_{2i}^{(a)}-J_{2j}^{(a)})=v_p(J_{2i+1}^{(a)}-J_{2j+1}^{(a)})=v_p(i-j).}
\]
Here \(v_p\) is the usual valuation of a nonzero integer, applied to its absolute value.

## Assumptions and scope

The base \(a\) is an arbitrary **even positive integer at least two**, \(n\) ranges over all nonnegative integers, and \(m\) ranges over all positive integers. For \(m=1\), the one residue is represented by definition. The criterion makes no assertion for odd bases. A prime divisor of \(1\) is understood vacuously.

The condition \(p\mid a+1\) does not mean \(m\mid a+1\): arbitrary powers of every prime dividing \(a+1\), and their arbitrary products, qualify. For example, at \(a=14\) all moduli \(3^u5^v\) for \(u,v\ge0\) qualify, along with \(2\).

## Proof

**Closed form.** The characteristic polynomial of the recurrence is
\[X^2-(a-1)X-a=(X-a)(X+1).\]
The initial conditions yield exactly the displayed formula, and divisibility of the numerator by \(a+1\) follows from \(a\equiv-1\pmod{a+1}\).

**Local isometries.** Fix an odd prime \(p\mid a+1\). Then \(a\equiv-1\pmod p\), so \(p\nmid a(a-1)\). Let \(i>j\ge0\) and write \(d=i-j\). The difference between even terms is
\[
J_{2i}^{(a)}-J_{2j}^{(a)}
=\frac{a^{2j}(a^{2d}-1)}{a+1}.
\]
The standard lifting-the-exponent lemma for odd \(p\mid a^2-1\) gives
\[
 v_p(a^{2d}-1)=v_p(a^2-1)+v_p(d)=v_p(a+1)+v_p(d),
\]
since \(p\nmid a-1\). Also \(p\nmid a\). Subtracting \(v_p(a+1)\) proves the even-indexed valuation identity. For odd terms the same calculation has an additional factor \(a\) in the numerator and gives the same identity. Reversing \(i,j\) changes only the sign of the differences.

**Surjectivity for supported odd moduli.** Let \(m=\prod p^e\) be odd with every \(p\mid m\) dividing \(a+1\). If \(0\le i<j<m\) and two even-indexed terms coincide modulo \(m\), the local identity implies \(p^e\mid j-i\) for every prime power of \(m\). Thus \(m\mid j-i\), impossible. The \(m\) even-indexed terms are therefore pairwise distinct and form a complete system. The identical argument applies to odd-indexed terms. The case \(m=1\) is immediate.

**Parity obstruction.** Since \(a\) is even, the recurrence or closed form shows that \(J_n^{(a)}\) is odd for every \(n\ge1\). Therefore modulo any even \(m\ge4\), the class \(2\pmod m\) never occurs: \(J_0^{(a)}=0\), and all later terms are odd. Modulo \(2\), both residues occur at indices zero and one.

**Prime obstructions.** Suppose \(p\) is an odd prime not dividing \(a+1\). If \(p\mid a\), then \(J_0^{(a)}=0\) but, for every \(n\ge1\), the closed form gives
\[J_n^{(a)}\equiv(-1)^{n+1}\pmod p.\]
At most \(0,1,-1\) occur. Thus only \(p=3\) can qualify. For \(p=3\mid a\), the values at \(n=0,1,2\) are \(0,1,a-1\equiv0,1,-1\pmod3\), so \(m=3\) really qualifies. If a modulus \(m>3\) is divisible by such a \(3\), the residue \(3\pmod m\) cannot occur: the only term divisible by \(3\) is \(J_0^{(a)}=0\). Hence no multiple of three larger than three qualifies in this case.

Finally, if \(p\nmid a(a+1)\), Fermat's theorem and the parity of \(p-1\) imply
\[J_{n+p-1}^{(a)}\equiv J_n^{(a)}\pmod p\qquad(n\ge0).\]
So there are at most \(p-1\) distinct residues modulo \(p\), and \(p\) is not complete. Any modulus with this prime factor cannot be complete by reduction modulo \(p\). The only primes left for an odd complete modulus, besides the isolated \(3\mid a\) case, are precisely the primes dividing \(a+1\); sufficiency was proved above.

## Verification

The accompanying standalone Python checker enumerates exact modular recurrence states and their eventual cycles. For each even base \(2\le a\le50\), it tests every \(1\le m\le120\), a total of \(3000\) complete-image decisions, against the closed criterion. It further tests the two parity permutations and the exact valuation-equivalent gcd identities over \(82\) supported odd base-modulus pairs in the same ranges, using integer arithmetic only.

Run \(`python3 verify_jacobsthal.py`\) to reproduce the output beginning with \(`VERIFY_OK`\). These finite computations are cross-checks; the proof above establishes the universal statement and does not rely on exhaustion.

## Relationship to prior work

Griffiths and Bramham, *The Jacobsthal Numbers: Two Results and Two Questions* (Fibonacci Quarterly 53(2), May 2015), Theorem 3.5, prove the complete-residue classification for the classical \(a=2\) Jacobsthal sequence: the complete moduli are \(2\) and all powers of \(3\). Their argument is a special-case precursor, and this finding makes **no originality claim** for \(a=2\). The present theorem uses variable even \(a\), gives arbitrary mixed-prime supported moduli such as \(3^u5^v\) for \(a=14\), classifies the isolated \(m=3\) case when \(3\mid a\), and proves exact local isometries and both parity permutations.

Bacani and Rabago (arXiv:1503.05301, first submitted March 18, 2015) use the Jacobsthal sequence as an example within a study of linear recurrences; their reported results do not provide the stated residue-modulus classification. Sriprad et al. (2015) treat a different parameterized recurrence \(J_{k,n}=kJ_{k,n-1}+2J_{k,n-2}\), and their common-factor identities do not imply the theorem for the split roots \(a,-1\).

## Limitations

The classification is restricted to **even integer bases**. It does not classify complete-modulus behavior for a general Lucas recurrence or odd bases. The \(a=2\) result was already published. A broader Lucas-sequence classification outside the examined literature might imply this theorem despite differing terminology, and no exhaustive worldwide literature survey or independent validation has been performed. The first fully day-stamped source used for the literature frame was publicly posted March 18, 2015; the closer Jacobsthal-completeness article is dated by issue only to May 2015.

## References

1. J. B. Bacani and J. F. T. Rabago, *On Linear Recursive Sequences with Coefficients in Arithmetic-Geometric Progressions*, arXiv:1503.05301, posted March 18, 2015. https://arxiv.org/abs/1503.05301
2. M. Griffiths and A. Bramham, *The Jacobsthal Numbers: Two Results and Two Questions*, Fibonacci Quarterly **53**(2) (May 2015), 147–151, Theorem 3.5. https://www.fq.math.ca/Papers1/53-2/GriffithsBramham11172014.pdf
3. W. Sriprad, W. Cherdchanpipat, K. Thaweesuksatien and P. Yordsorn, *Generalized identities involving common factors of k-Generalized Fibonacci, k-Jacobsthal and k-Jacobsthal-Lucas numbers*, Science and Technology RMUTT Journal **5**(1) (2015), 77–82, first-published June 30, 2015. https://ph02.tci-thaijo.org/index.php/past/article/view/243209

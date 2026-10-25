# Exact Frobenius numbers for all nontrivial odd-parameter Proth semigroups

## Finding
For every integer \(n\ge3\) and odd integer \(m\) with \(3\le m<2^n\), put \(M=m2^n\) and
\[
P_m(n)=\big\langle m2^{n+i}+1:i\in\mathbb Z_{\ge0}\big\rangle.
\]
Write \(h=s_2(m)\) for the number of ones in the binary expansion of \(m\). Greedily decompose \(h\) using coins \(b_i=2^i-1\), \(i\ge1\), with the largest coin at each stage; thus
\[
h=\sum_{i\ge1}y_i b_i,\qquad c=\sum_{i\ge1}y_i,\qquad t=\min\{i:y_i>0\}.
\]
The sum is finite and \(t\) exists because \(h\ge2\). The **exact Frobenius number**, the largest nonnegative integer outside this semigroup, is
\[
\boxed{F(P_m(n))=M^2+(h+c-1)M+(h+c+t-2).}
\]
Moreover, the unique maximal element of the Apéry set modulo \(M+1\) belongs to residue class \(-(M-t+1)\) modulo \(M+1\). In particular, its reduced linear and constant coefficients depend on \(m\) only through its binary popcount. One previously uncomputed branch is \(n=7,m=127\), where \(h=7,c=1,t=3,M=16256\) and \(F=264371337\).

## Assumptions and scope
The exponent \(n\) is an integer at least three; \(m\) is odd, positive, at least three, and strictly smaller than \(2^n\). The index in the semigroup generating set includes zero. The greedy expansion of a nonnegative integer \(u\) by \(b_i=2^i-1\) means repeatedly taking as many copies of the largest available \(b_i\) as possible, continuing down to \(b_1=1\). This definition is unambiguous. The Frobenius number is finite because the semigroup has multiplicity \(M+1\) and contains an element congruent to \(-1\) modulo it.

## Proof
**1. Published Apéry reduction and optimality.** Let \(r=\lfloor\log_2m\rfloor\), \(k=n+r\), \(a=M+1\) and \(b_i=2^i-1\). The minimal generating family for the Proth semigroup is \(a\) and \(2^ia-b_i\), for \(1\le i\le k\). By Liu–Xin–Ye–Yin, Theorem 5.2, for each \(0\le u\le M\) the minimum element in the residue class \(-u\pmod a\) is
\[
N_{-u}=a\,w(u)-u,\qquad w(u)=\sum_{i=1}^k 2^i x_i(u),
\]
where \(x_i(u)\) are the greedy \(b_i\)-coin digits of \(u\). Their Lemma 2.6 guarantees this greedy coin count is optimal, and the identity \(2^i=b_i+1\) gives \(w(u)=u+\sum_i x_i(u)\). The standard Apéry formula is \(F(P_m(n))=\max_{0\le u\le M}N_{-u}-a\).

For completeness, \(w(u)\) is nondecreasing in \(u\). Starting from a minimum-weight coin representation of \(u+1\), remove one \(b_1\) if it has one, or replace one coin \(b_i\), \(i\ge2\), by two copies of \(b_{i-1}\). The identity \(b_i-1=2b_{i-1}\) makes this a representation of \(u\) with weight no larger than the original: removing \(b_1\) lowers weight by two, and the replacement preserves weight because \(2^i=2\cdot2^{i-1}\). Greedy weight is minimal, so \(w(u)\le w(u+1)\).

**2. Binary digits become the high greedy coins.** Write \(m=\sum_{j=0}^{r}e_j2^j\), with \(e_j\in\{0,1\}\). In greedy division of \(M\), the coefficients of \(b_{n+j}\), from \(j=r\) down to zero, are exactly \(e_j\). Indeed, after the indices greater than \(j\) have been removed, the remainder is
\[
R_j=\sum_{\ell=0}^{j}e_\ell2^{n+\ell}+\sum_{\ell=j+1}^{r}e_\ell.
\]
If \(e_j=0\), the bound \(R_j\le(2^j-1)2^n+r-j<b_{n+j}\) forces a zero coefficient. If \(e_j=1\), the bounds \(b_{n+j}\le R_j<2b_{n+j}\), valid because \(r\le n-1\) and \(n\ge3\), force coefficient one. After removing all these high coins, the remainder equals \(h=\sum_j e_j\le n<2^n-1=b_n\). Hence all remaining coins have indices below \(n\) and are precisely the greedy expansion of \(h\). It follows that the entire greedy coin count for \(M\) is \(h+c\), its lowest occupied index is \(t\), and
\[
w(M)=M+h+c.
\]

**3. The last flat segment of the greedy weight.** For each \(i\ge1\), the greedy weight of \(b_i-j\) equals \(2^i\) when \(0\le j<i\), and equals \(2^i-2\) when \(j=i\). For \(i=1\), this is direct. For \(i\ge2\), the identity \(b_i-1=2b_{i-1}\) proves the case \(j=1\); for \(2\le j\le i\), use the greedy decomposition
\[
b_i-j=b_{i-1}+(b_{i-1}-(j-1)),
\]
and induction on \(i\). The displayed representation is greedy because the remainder is strictly below \(b_{i-1}\). Thus, if the lowest occupied coin of \(M\) has index \(t\), subtraction of \(j\), for \(0\le j\le t\), changes only one copy of \(b_t\). It follows that
\[
w(M-j)=w(M)\quad(0\le j<t),\qquad w(M-t)=w(M)-2.
\]
By monotonicity, the top weight occurs exactly for \(M-t+1\le u\le M\). For \(u\le M-t\) the weight is at most \(w(M)-2\); since \(0\le u\le M<a\), such residues cannot attain the largest value of \(a\,w(u)-u\). On the top-weight plateau this expression decreases strictly with \(u\), hence it has the **unique** maximum at \(u_*=M-t+1\).

**4. Evaluation.** Substituting \(u_*\) and \(w(M)=M+h+c\) into the Apéry formula gives
\[
\begin{aligned}
F(P_m(n))&=(M+h+c)(M+1)-(M-t+1)-(M+1)\\
&=M^2+(h+c-1)M+(h+c+t-2).
\end{aligned}
\]
The same argument gives the asserted unique maximizing residue.

## Verification
Run `python3 verification/check_proth.py` from the package root. An independent shortest-path computation over the residue graph for the original semigroup generators checks the claimed Frobenius number and unique Apéry maximizer for 161 admissible parameter pairs, covering 1,072,169 residue vertices. The program checks three additional larger first-omitted-branch examples and all local carry identities through coin index 25, with assertion failures on disagreement. These finite computations corroborate but do not replace the preceding infinite proof. The proof relies on published Apéry and greedy optimality results for the original family, whose parameter conditions are explicitly matched above.

## Relationship to prior work
Srivastava–Thakkar (2023), *The Frobenius Problem for the Proth Numbers*, develops the family and obtains a Frobenius formula for its restricted odd parameter of the form \(2^r+1\). Liu–Xin–Ye–Yin (2023; revised manuscript 2025), *On the Frobenius Number and Genus of a Collection of Semigroups Generalizing Repunit Numerical Semigroups*, gives the full-family Apéry and genus reductions, but its explicitly evaluated Frobenius formulas in Theorems 5.4 and 5.5 require respectively a nonzero first greedy coefficient or a zero first coefficient and nonzero second one. The authors explicitly note the missed case \(q=63\), for which the first two greedy coefficients vanish. Their paper supplies necessary foundations but not the universal binary-popcount formula nor the arbitrary-depth plateau argument. The present theorem uses those foundations to evaluate the remaining maximization for every allowable odd parameter, including all cases of multiple initial zero coefficients.

## Limitations
The statement concerns the standard Proth numerical semigroup at integer exponents \(n\ge3\) and odd \(m\) strictly between \(1\) and \(2^n\); no formula for generalized bases or perturbed generator sets is asserted. The earlier full-family Apéry/greedy theorem is used as a proven input rather than reproved wholesale. No separate genus, type, or pseudo-Frobenius classification is claimed. Literature comparison is limited to the accessible sources described, and an earlier unindexed equivalent formula cannot be excluded by search alone.

## References
1. F. Liu, G. Xin, S. Ye and J. Yin, *On the Frobenius Number and Genus of a Collection of Semigroups Generalizing Repunit Numerical Semigroups*, arXiv:2306.03459 (initial public manuscript 2023-06-06), particularly Lemmas 2.6 and 2.11 and Theorems 5.2, 5.4 and 5.5; full text: https://arxiv.org/pdf/2306.03459.
2. P. Srivastava and D. Thakkar, *The Frobenius Problem for the Proth Numbers*, arXiv:2311.12462 (2023-11-21), https://arxiv.org/pdf/2311.12462.

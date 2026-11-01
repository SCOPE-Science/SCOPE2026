# Exact \(p\)-kernel rank of prime-power Pascal-row counts

## Finding
For a prime \(p\), an integer \(\alpha\ge1\), and \(n\ge0\), define
\[
a_{p,\alpha}(n)=\#\bigl\{k\in\{0,\ldots,n\}:p^\alpha\nmid\binom{n}{k}\bigr\}.
\]
The rational \(p\)-kernel of this sequence has **exact rank**
\[
\boxed{\operatorname{rank}_{\mathbb Q}\{n\mapsto a_{p,\alpha}(p^e n+r):e\ge0,\ 0\le r<p^e\}=2\alpha-1.}
\]
This gives the sharp minimal state dimension of a rational linear base-\(p\) representation, uniformly in the prime \(p\). Rowland [1, final paragraph] explicitly proposed this rank in 2010 as an open problem; the matrix product subsequently established in [2] supplies the upper-dimensional framework, whereas the lower bound requires the reachability and observability proof below.

## Assumptions and scope
The prime \(p\) is arbitrary and fixed; \(\alpha\) is a positive integer. All ranks and linear combinations are over \(\mathbb Q\). The \(p\)-kernel comprises the sequences \((a_{p,\alpha}(p^e n+r))_{n\ge0}\) for \(e\ge0\) and \(0\le r<p^e\). A digit word \(w=(d_0,\ldots,d_{e-1})\) is always read from *least* to *most* significant digit, and its value is \(\operatorname{val}_p(w)=\sum_{i=0}^{e-1}d_i p^i\). The empty word is allowed; padding a prefix with zero digits is meaningful for the kernel. The zero integer has the empty digit expansion.

For a polynomial \(H(z)\) of degree below \(\alpha\), \(H(1)\) means the sum of its coefficients. All products below are performed modulo \(z^\alpha\). Write \(\mathcal P_{<\alpha}=\mathbb Q[z]/(z^\alpha)\).

## Proof
**1. A digit representation from Kummer's theorem.** Let
\[
W=\mathcal P_{<\alpha}\oplus z\mathcal P_{<\alpha},
\qquad \dim_{\mathbb Q}W=\alpha+(\alpha-1)=2\alpha-1.
\]
Represent a state as \((U,V)\), where \([z^j]U\) counts choices of already-read digits of \(k\) causing exactly \(j\) borrows and leaving no outgoing borrow, and \([z^j]V\) counts choices leaving an outgoing borrow. Initially \((U,V)=(1,0)\). A digit \(d\in\{0,\ldots,p-1\}\) of \(n\) induces
\[
T_d(U,V)=\bigl((d+1)U+dV,\ z((p-1-d)U+(p-d)V)\bigr)\pmod{z^\alpha}.
\]
Indeed, if the entering borrow is zero, precisely \(d+1\) digits of \(k\) avoid a new borrow and \(p-1-d\) produce one. If the entering borrow is one, the corresponding numbers are \(d\) and \(p-d\). Every new borrow contributes one factor of \(z\). Thus the outgoing-borrow series lies in \(z\mathcal P_{<\alpha}\).

After the digits of \(n\), the numbers \(k\le n\) are exactly those with no outgoing borrow. By Kummer's theorem, the number of borrows equals the \(p\)-adic valuation of \(\binom{n}{k}\). Therefore the output functional
\[
\lambda(U,V)=U(1)
\]
recovers \(a_{p,\alpha}(n)\). For every prefix \(w\), its state \(s_w=T_{d_{e-1}}\cdots T_{d_0}(1,0)\) defines the kernel subsequence \(n\mapsto a_{p,\alpha}(p^e n+\operatorname{val}_p(w))\) by applying the remaining higher digits of \(n\) and then \(\lambda\). This establishes the rank bound \(\le2\alpha-1\).

**2. Reachability.** Let \(s_r=T_0^r(1,0)\) for \(r\ge0\). Direct substitution gives
\[
s_r=\left(1,(p-1)\sum_{j=1}^{\min(r,\alpha-1)}p^{j-1}z^j\right).
\]
For \(1\le r\le\alpha-1\),
\[
s_r-s_{r-1}=(0,(p-1)p^{r-1}z^r).
\]
Since \(p\ge2\), the reachable state span contains every \((0,z^r)\) with \(1\le r\le\alpha-1\), together with \((1,0)\). Furthermore,
\[
T_{p-1}(0,z^r)=((p-1)z^r,z^{r+1}),
\]
where the final term is zero when \(r=\alpha-1\). Subtract the already reachable vector \((0,z^{r+1})\) to obtain every \((z^r,0)\). The reachable span is thus **all of** \(W\); the argument includes \(\alpha=1\), when \(W\) is spanned by \((1,0)\).

**3. Observability.** Suppose \((U,V)\in W\) yields zero under \(\lambda\) after *every* finite continuation digit word. For \(h=0,\ldots,\alpha-1\), let \(y_h\) be the output after \(h\) digits all equal to \(p-1\). Under such a digit,
\[
U\longmapsto pU+(p-1)V,\qquad V\longmapsto zV.
\]
Hence
\[
y_0=U(1)=0,\qquad y_h-py_{h-1}=(p-1)\sum_{j=1}^{\alpha-h}[z^j]V\quad(1\le h\le\alpha-1).
\]
All these sums vanish. Reading them from \(h=\alpha-1\) down to \(h=1\) yields every coefficient of \(V\) equal to zero. Now prepend a digit zero to those continuations. With \(V=0\), digit zero transforms \((U,0)\) to \((U,(p-1)zU)\). Let \(y'_h\) be the output after that zero digit and then \(h\) digits equal to \(p-1\). Again all outputs vanish, and
\[
y'_h-py'_{h-1}=(p-1)^2\sum_{j=0}^{\alpha-h-1}[z^j]U\quad(1\le h\le\alpha-1).
\]
These nested sums yield the coefficients of \(U\) in degrees \(0,\ldots,\alpha-2\) equal to zero. Finally \(U(1)=0\) gives the last coefficient zero. Thus the only unobservable state is \((0,0)\), including at \(\alpha=1\).

**4. Exact kernel rank and minimality.** The linear map from \(W\) to functions on higher-digit continuations, \(s\mapsto(w\mapsto\lambda(T_w s))\), is injective by step 3. The reachable vectors from kernel prefixes span \(W\) by step 2. Consequently the kernel functions span an injective image of \(W\), so their rational rank is exactly \(\dim W=2\alpha-1\). Every rational linear digit representation of the same sequence must have dimension at least its kernel rank; the constructed representation attains this minimum.

## Verification
The accompanying `verify_rank.py` uses exact rational elimination. For \(p\in\{2,3,5\}\) and \(1\le\alpha\le6\), it (a) directly evaluates Pascal-row coefficients modulo \(p^\alpha\); (b) constructs \(2\alpha-1\) reachable prefix states; (c) evaluates \(2\alpha-1\) suffix observations; (d) checks that both resulting state and Hankel matrices have full rank; and (e) verifies the corresponding direct \(p\)-kernel sample matrix. All 18 parameter pairs pass. The theorem is proved for every prime and exponent by the preceding symbolic argument; finite experiments are not used to infer universality.

## Relationship to prior work
Rowland [1] developed subword-based formulas for \(a_{p,\alpha}(n)\) and explicitly left the exact \(p\)-regular rank \(2\alpha-1\) open. Spiegelhofer and Wallner [3] studied efficient generating functions for the exact-valuation coefficient polynomials and explicitly set aside the \(p\)-regular line of investigation. Rowland [2, Theorem 1] later provided a \(2\times2\) matrix product over \(\mathbb Z[z]\) for all valuation strata simultaneously; its degree-\(\alpha\) truncation is a natural upper-bound construction. This result supplies a proof of the **matching lower bound**, showing the truncated carry/borrow representation cannot be reduced. Kummer's theorem and the earlier matrix construction are acknowledged, not claimed as new. The main novelty is the unrestricted exact minimality and resolution of the stated rank question.

## Limitations
The theorem is over characteristic-zero rational scalars. It does not determine the dimension over finite coefficient fields, the minimal size of a deterministic finite automaton for a reduction of the sequence, or analogous exact ranks for multinomial counts. A mathematically equivalent minimal-rank theorem in specialized earlier literature would affect historical originality; the primary-source comparison is not a universal priority certificate.

## References
1. Eric Rowland, *The number of nonzero binomial coefficients modulo \(p^\alpha\)*, arXiv:1001.1783, first posted 2010-01-12; see the final paragraph of Section 3. https://arxiv.org/abs/1001.1783
2. Eric Rowland, *A matrix generalization of a theorem of Fine*, arXiv:1704.05872, first posted 2017-04-19, Theorem 1 and Section 1. https://arxiv.org/html/1704.05872v2
3. Lukas Spiegelhofer and Michael Wallner, *An explicit generating function arising in counting binomial coefficients divisible by powers of primes*, arXiv:1604.07089, first posted 2016-04-24, Introduction and Section 2. https://arxiv.org/abs/1604.07089
4. Jean-Pierre Allouche and Jeffrey Shallit, *The ring of \(k\)-regular sequences*, Theoret. Comput. Sci. 98 (1992), 163–197, general framework for kernel rank.

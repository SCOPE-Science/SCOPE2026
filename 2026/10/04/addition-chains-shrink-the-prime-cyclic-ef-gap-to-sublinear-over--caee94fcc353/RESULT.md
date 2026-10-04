# Addition chains shrink the prime-cyclic EF gap to sublinear overhead

## Finding
Work in Gomaa's relational group language \(L_G=(R,e)\), where \(R(x,y,z)\) means \(x+y=z\) and \(e\) names the identity. For an integer \(m\ge1\), let \(\ell(m)\) be the minimum length of an addition chain
\[
1=a_0<a_1<\cdots<a_r=m,\qquad a_i=a_j+a_k\quad(j,k<i),
\]
so \(\ell(m)=r\). For an odd prime \(p\), define
\[
\Lambda(p)=\min\{\ell(p),\ \ell(p+1),\ \ell(p-1)+1\}.
\]
Then for every pair of primes \(p<q\), Spoiler wins the Ehrenfeucht--Fraisse game on \(\mathbb Z_p\) and \(\mathbb Z_q\) in at most \(\Lambda(p)\) rounds, with every move played in \(\mathbb Z_p\). Equivalently, there is an existential \(L_G\)-sentence of quantifier rank at most \(\Lambda(p)\) distinguishing the two groups.

If \(2^n<p<2^{n+1}\), Gomaa's lower bound therefore combines with this construction to give
\[
n+1\le d(p,q)\le \Lambda(p)\le \ell(p),
\]
where \(d(p,q)\) is the least distinguishing quantifier rank. Yao's classical addition-chain bound implies a universal constant \(C\) for which
\[
\ell(p)\le \log_2 p + C\,\frac{\log p}{\log\log(p+2)}.
\]
Consequently
\[
d(p,q)\le n+1+O\!\left(\frac{n}{\log n}\right),
\]
uniformly for primes \(q>p\). Thus the factor-two upper bound in the archived source can be replaced, in the prime-order case, by a \(1+O(1/\log n)\) factor over the known lower bound. In particular, whenever \(\Lambda(p)=n+1\), the exact distinguishing rank is \(n+1\).

## Proof of the addition-chain transfer
First take an addition chain \(1=a_0<a_1<\cdots<a_r=p\). For each \(i<r\), Spoiler selects the element \(a_i\bmod p\) in \(\mathbb Z_p\). These are distinct nonidentity elements because \(1\le a_i<p\). Whenever \(a_i=a_j+a_k\) with \(i<r\), the selected tuple satisfies the atomic relation \(R(a_j,a_k,a_i)\). For the final step \(p=a_j+a_k\), the tuple satisfies \(R(a_j,a_k,e)\).

Suppose Duplicator's response to \(a_0=1\) in \(\mathbb Z_q\) is \(y\). Inductively, preservation of the chain relations forces the response to each selected \(a_i\) to be \(a_i y\). The final atomic relation then gives \(py=0\) in \(\mathbb Z_q\). Since \(p\ne q\) and \(q\) is prime, multiplication by \(p\) is injective on \(\mathbb Z_q\), so \(y=0\). But \(a_0\ne e\) in \(\mathbb Z_p\), whereas equality to the named identity is atomic. Hence Duplicator cannot preserve the atomic diagram. This gives a win in \(r=\ell(p)\) rounds.

Now let \(1=a_0<\cdots<a_r=p+1\) be an addition chain. If the chain contains \(p\) as an earlier entry, truncate at that entry and use the previous argument; this wins in fewer than \(r\) rounds. Otherwise all \(a_0,\ldots,a_{r-1}\) lie in \(\{1,\ldots,p-1\}\). Select those \(r\) residues. If the last chain step is \(p+1=a_j+a_k\), then modulo \(p\) the closing atomic relation is \(R(a_j,a_k,a_0)\). In a response tuple over \(\mathbb Z_q\), chain preservation again forces coefficient multiples of \(y\), and the closing relation gives \((p+1)y=y\), hence \(py=0\). The same contradiction follows, so \(d(p,q)\le\ell(p+1)\).

Finally take a chain \(1=a_0<\cdots<a_r=p-1\). Select every chain entry, using \(r+1=\ell(p-1)+1\) rounds. The chain relations force the response to \(a_r\) to be \((p-1)y\), while the additional true atomic relation \(R(a_r,a_0,e)\) forces \(py=0\). This proves the \(\ell(p-1)+1\) alternative and hence the \(\Lambda(p)\) bound.

Because every move is on the \(\mathbb Z_p\) side, the standard EF correspondence yields an existential distinguishing sentence with the same quantifier rank.

## Quantitative consequence
Gomaa proves that if \(2^n<p<2^{n+1}\) and \(p<q\) are prime, every distinguishing sentence has quantifier rank at least \(n+1\), while the dissertation's general prime-order construction gives an upper bound \(2n\) and explicitly asks whether the gap can be improved. The same chapter exhibits special sparse binary congruence systems attaining the lower bound for some prime families.

The present transfer replaces the particular binary binder by an arbitrary addition chain. For a singleton exponent, Yao's power-evaluation theorem gives an addition chain of length
\[
\log_2 p+O\!\left(\frac{\log p}{\log\log p}\right).
\]
Since \(\log_2 p<n+1\) and \(\log p\asymp n\), this is \(n+1+O(n/\log n)\). The result is therefore asymptotically stronger than both Gomaa's \(2n\) construction and the explicit signed-binary \(n+\lceil n/2\rceil\) refinement recorded in the immediately preceding ledger finding.

## Verification
The accompanying `verify.py` checks the translation from concrete addition chains to atomic \(L_G\)-relations. It validates generic binary chains for every odd prime below 20,000, checks all selected coefficients are distinct and nonidentity before the closing step, and separately exercises the \(p\), \(p+1\), and \(p-1\) closures. It also verifies that each closing relation algebraically yields a coefficient exactly divisible by \(p\). The finite computation is corroborative only; the theorem is the symbolic argument above plus the cited classical addition-chain bound.

## Relationship to prior work
The primary archived source is Walid Gomaa's 2007 dissertation. Its prime-order chapter proves the \(n+1\) lower bound and \(2n\) upper bound for \(2^n<p<2^{n+1}<q\) in the relevant notation, states that narrowing the gap is open, and gives several exact sparse-binary examples. Its general upper construction is a particular binary realization of a closed binder; it does not state an upper bound in terms of minimal addition-chain length or derive a sublinear additive gap.

Andrew Yao's 1976 power-evaluation theorem is classical addition-chain theory, not finite model theory. For one exponent it supplies the \(\log p+O(\log p/\log\log p)\) chain length used here. Searches of the archived source, published-finding corpus, and the public web found no source combining this addition-chain bound with Gomaa's EF game to obtain \(n+O(n/\log n)\) quantifier rank for prime cyclic groups.

## Limitations
The proof is for distinct prime-order cyclic groups. For composite target groups, the equation \(py=0\) can have nonzero solutions, so the same short chain does not by itself uniquely identify the cyclic group; Gomaa's subgroup-excluding binders address that harder setting. The result also makes no bounded-variable claim: an arbitrary short addition chain can require more simultaneously named variables than Gomaa's separate five-variable construction.

Priority risk remains for unindexed later notes or theses that may have noticed the addition-chain connection without using the searched terminology.

## References
1. Walid Gomaa, *Model Theory and Complexity Theory*, PhD dissertation, University of Maryland, 2007, Chapter 3, especially Theorem 3.3, Lemma/Theorem 3.4, Corollary 3.3, Theorems 3.5--3.6, and Section 3.9. Handle: 1903/7227.
2. Andrew Chi-Chih Yao, *On the Evaluation of Powers*, SIAM Journal on Computing 5(1) (1976), 100--103. DOI: 10.1137/0205008.
3. Alfred Brauer, *On Addition Chains*, Bulletin of the American Mathematical Society 45(10) (1939), 736--739. DOI: 10.1090/S0002-9904-1939-07068-7.

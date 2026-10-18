# Pseudo-Frobenius spectrum of the \(2^n+1\) companion semigroups

## Finding
For every integer \(n\ge3\), put \(a=2^n+1\) and define the numerical semigroup
\[S_n=\langle a,\;2^i(a+1)-1:\ 1\le i\le n-1\rangle.\]
Its set of pseudo-Frobenius numbers is exactly
\[\operatorname{PF}(S_n)=\{a^2+3a-1\}\cup\{a^2-a-1-j:4\le j\le n\}.\]
The second set is empty at \(n=3\). Thus the type is \(n-2\); at \(n=3\) the semigroup is symmetric. The formula separates a terminal block of \(n-3\) gaps from the Frobenius number.

## Assumptions and scope
Here \(\mathbb N=\{0,1,\ldots\}\); a numerical semigroup is an additive submonoid of \(\mathbb N\) with finite complement. A pseudo-Frobenius number is an integer \(z\notin S_n\) such that \(z+s\in S_n\) for every nonzero \(s\in S_n\). The type is their number. The first two generators \(a\) and \(2a+1\) are coprime, so \(S_n\) is numerical. All quantifiers range over integers \(n\ge3\). No primality of \(a\) is assumed: the name refers only to its binary shape.

## Proof
Write \(m=n-1\) and \(c_i=2^i-1\) for \(1\le i\le m\). A generator other than \(a\) equals \((a+1)c_i+a\). Let \(t_h(r)\) be the minimum number of coins of denominations \(c_1,\ldots,c_h\) needed to make \(r\), counting a repeated denomination repeatedly; put \(t_h(0)=0\). These repunit denominations form a canonical greedy coin system [1, Lemma 3.1], so the algorithm taking as many of the largest coin as possible computes \(t_h\). The published Apéry formula [1, Lemma 3.3, Equation (4)] applies because \(\gcd(a,1)=1\) and \(a\ge m-1\): the minimum semigroup member \(w(r)\equiv r\pmod a\), for \(0\le r<a\), is
\[w(r)=(a+1)r+a\,t_m(r).\tag{1}\]
This formula is a cited premise; the novel part below classifies its maximal elements in the semigroup order for \(a=2^n+1\).

**Greedy local-maxima lemma.** For \(h\ge1\), put \(C_h=2^h-1\) and \(R_h=2C_h\). A position \(0\le r\le R_h\) is *jump-maximal* when \(t_h(r+c_i)\le t_h(r)\) for every \(1\le i\le h\) with \(r+c_i\le R_h\). Then the jump-maximal positions are exactly
\[R_h-h+1,\ R_h-h+2,\ldots,R_h.\tag{2}\]
Furthermore, for each \(0\le q\le h-1\),
\[t_h(R_h-q)=q+2.\tag{3}\]
Both assertions follow simultaneously by induction. For \(h=1\), only unit coins occur, and direct inspection of \(0,1,2\) establishes both. For \(h\ge2\), greedy decomposition gives \(t_h(r+C_h)=t_h(r)+1\) whenever \(0\le r\le C_h\); hence no jump-maximal position lies at or below \(C_h\). Any remaining position strictly below \(2C_h\) is \(C_h+y\) with \(1\le y\le C_h-1=2C_{h-1}\), and has \(t_h(C_h+y)=1+t_{h-1}(y)\). For a jump by \(c_i\) with \(i<h\), if \(y+c_i<C_h\), the inequality is precisely the corresponding inequality for \(t_{h-1}\) at \(y\). If \(y+c_i=C_h\), its target has coin count \(t_h(2C_h)=2\), never exceeding \(1+t_{h-1}(y)\); larger jumps leave the interval. Hence the jump-maximal positions strictly below \(2C_h\) are \(C_h\) plus the jump-maximal positions for \(t_{h-1}\) on \([0,2C_{h-1}]\). Appending \(2C_h\) yields (2). For (3), \(q=0\) is immediate, while for \(1\le q\le h-1\), the greedy relation and \(C_h=2C_{h-1}+1\) give
\[t_h(2C_h-q)=1+t_{h-1}(2C_{h-1}-(q-1))=1+(q+1)=q+2.\]

Now \(a-1=2^n=2C_m+2\), and the greedy rule gives
\[t_m(2C_m)=2,\quad t_m(2C_m+1)=3,\quad t_m(2C_m+2)=4.\tag{4}\]
For each \(r\in[0,a-1]\), the gap \(w(r)-a\) is pseudo-Frobenius exactly when \(w(r)-a+g\in S_n\) for every generator \(g\ne a\). If \(r+c_i<a\), use (1) to obtain
\[w(r)+((a+1)c_i+a)-w(r+c_i)=a\bigl(t_m(r)+1-t_m(r+c_i)\bigr).\]
Thus this condition is equivalent to \(t_m(r+c_i)\le t_m(r)\). If \(r+c_i\ge a\), write \(r'=r+c_i-a\); the same difference is \(a\bigl(a+2+t_m(r)-t_m(r')\bigr)\), at least \(a\), because \(t_m(r')\le r'\le a-1\). So wrapping jumps impose no further restriction. The pseudo-Frobenius residues are exactly the jump-maximal positions for \(t_m\) on \([0,a-1]\).

Any \(r\le C_m+2\) is eliminated by adding \(C_m\): its greedy coin count increases by one. On \(C_m+3\le r\le2C_m-1\), write \(r=C_m+y\). The reductions used to prove (2) show that the candidates are
\[r=2C_m-j+2=(a-1)-j,\qquad 3\le j\le m+1=n.\tag{5}\]
Indeed, (2) for \(h=m-1\) gives \(C_m-m+1\le y\le C_m-1\). The upper endpoint \(r=(a-1)-3\) is *not* maximal: by (3) its coin count is three, whereas adding \(c_2=3\) reaches \(a-1\), with coin count four. For every remaining \(r=(a-1)-j\), \(4\le j\le n\), equation (3) gives \(t_m(r)=j\ge4\). Jumps remaining below \(2C_m\) cannot increase this count, by (2). Jumps into the top three residues have counts at most four by (4), and therefore cannot increase it either. Finally, among \(2C_m,2C_m+1,2C_m+2\), equation (4) shows that adding \(c_1=1\) eliminates the first two and the last position \(a-1\) is maximal. Thus the complete pseudo-Frobenius residue set is
\[\{a-1\}\cup\{a-1-j:4\le j\le n\}.\tag{6}\]
By (1), for \(4\le j\le n\), \(t_m(a-1-j)=j\), whence \(w(a-1-j)-a=a^2-a-1-j\). At \(r=a-1\), equation (4) yields \(w(a-1)-a=a^2+3a-1\). This proves the claimed set and type. For \(n=3\) the type is one, hence the numerical semigroup is symmetric, by the standard pseudo-Frobenius characterization.

## Verification
The accompanying `verify_fermat_companion.py` checks equation (2) and (3) for \(1\le h\le12\), independently reconstructs Apéry sets by residue-graph shortest paths for \(3\le n\le11\), compares the full sets of pseudo-Frobenius numbers and checks (1) on every residue. It passed 16,368 finite greedy-cutoff tests and 4,097 Apéry entries. Run `python verify_fermat_companion.py` with Python 3 and no third-party dependencies. These tests are not a substitute for the proof over all \(n\).

## Relationship to prior work
Liu, Xin, Ye, and Yin [1] establish the greedy coin property and the general Apéry formula, and classify pseudo-Frobenius numbers when the first generator is a repunit \((b^n-1)/(b-1)\). Their special-case theorem does not have the first generator \(2^n+1\). Branco, Colaço, and Ojeda [2] classify type and pseudo-Frobenius numbers of a separate generalized-repunit family in which the first generator is a base-\(b\) repunit; it likewise does not provide this \(n\)-generator companion family. The known Frobenius formula from the general Apéry method is not claimed as original here. The distinguishing contribution is the complete set (6), including a drop in type from the repunit/Mersenne family to \(n-2\).

## Limitations
This classifies only the indicated binary-shifted generator family, not arbitrary \(a,d,b,k\) in [1]. It relies on the cited, published greedy/Apéry lemmas. Literature search and accessible-result comparisons cannot guarantee that no equivalent unpublished or unindexed derivation exists. No independent mathematical audit has been performed.

## References
[1] F. Liu, G. Xin, S. Ye, J. Yin, *A Note on Generalized Repunit Numerical Semigroups*, arXiv:2306.10738v1 (first publicly submitted 2023-06-19), especially Lemmas 3.1 and 3.3 and Theorem 4.3. https://arxiv.org/html/2306.10738v1

[2] M. B. Branco, I. Colaço, I. Ojeda, *The Frobenius Problem for Generalized Repunit Numerical Semigroups*, Mediterranean Journal of Mathematics 20 (2023), article 16, online 2022-12-03. https://doi.org/10.1007/s00009-022-02233-w

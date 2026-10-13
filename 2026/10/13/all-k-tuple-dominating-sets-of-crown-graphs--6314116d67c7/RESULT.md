# All \(k\)-tuple dominating sets of crown graphs

## Finding
For every integer \(n\ge3\), let \(\operatorname{Cr}_n=K_{n,n}-M\) have bipartition \(A=\{a_1,\ldots,a_n\}\), \(B=\{b_1,\ldots,b_n\}\), with deleted perfect matching \(M=\{a_i b_i:1\le i\le n\}\). For \(S\subseteq V(\operatorname{Cr}_n)\), put \(P=\{i:a_i\in S\}\), \(Q=\{i:b_i\in S\}\), \(p=|P|\), and \(q=|Q|\). For every \(1\le k\le n\), \(S\) is a \(k\)-tuple dominating set if and only if either \(k=1\) and \(S=A\) or \(S=B\), or else \(p,q\ge k\), with \(p=k\Rightarrow P\subseteq Q\) and \(q=k\Rightarrow Q\subseteq P\). If \(I_{n,k}(z)=\sum_{j=k+1}^{n}\binom{n}{j}z^j\), then the bivariate side-profile enumerator is
\[
F_{n,k}(u,v)=I_{n,k}(u)I_{n,k}(v)+\binom{n}{k}(uv)^k\big((1+u)^{n-k}+(1+v)^{n-k}-1\big)+\mathbf 1_{k=1}(u^n+v^n).
\]
Hence the ordinary cardinality enumerator is
\[
D_{\times k}(\operatorname{Cr}_n;x)=I_{n,k}(x)^2+\binom{n}{k}x^{2k}\big(2(1+x)^{n-k}-1\big)+2\mathbf 1_{k=1}x^n.
\]
In particular, \(\gamma_{\times k}(\operatorname{Cr}_n)=2k\), and exactly \(\binom{n}{k}\) minimum \(k\)-tuple dominating sets occur, namely the sets with \(P=Q\) and \(|P|=k\). No \(k\)-tuple dominating set exists for \(k>n\).

## Assumptions and scope
All graphs are finite, simple, and undirected. The crown graph \(\operatorname{Cr}_n\) is \(K_{n,n}\) with one perfect matching deleted, and throughout \(n\ge3\). A \(k\)-tuple dominating set is a set \(S\) such that \(|N[v]\cap S|\ge k\) for every vertex \(v\). Since every closed neighborhood in \(\operatorname{Cr}_n\) has cardinality \(n\), only \(1\le k\le n\) is feasible.

The polynomial \(F_{n,k}(u,v)\) records a set \(S\) with weight \(u^{|S\cap A|}v^{|S\cap B|}\). Its specialization \(u=v=x\) is the ordinary cardinality enumerator.

## Proof
Fix \(S\), and write \(P,Q,p,q\) as above. For an index \(i\), define
\[
d_i=\mathbf 1_{i\in P}-\mathbf 1_{i\in Q}\in\{-1,0,1\}.
\]
Because \(a_i\) is adjacent to every vertex of \(B\) except \(b_i\),
\[
|N[a_i]\cap S|=q+d_i.
\]
Similarly,
\[
|N[b_i]\cap S|=p-d_i.
\]
Thus \(S\) is \(k\)-tuple dominating exactly when
\[
q+d_i\ge k,\qquad p-d_i\ge k
\]
for every \(i\).

Suppose first that the exceptional one-sided case does not occur. If \(q\le k-2\), then \(q+d_i\le k-1\), impossible. If \(q=k-1\), then every \(d_i\) must equal \(1\), forcing \(P=[n]\) and \(Q=arnothing\). Hence \(q=0\) and therefore \(k=1\), which is exactly the exceptional set \(A\). Thus outside that exception \(q\ge k\). The symmetric argument gives \(p\ge k\), except for the exceptional set \(B\) when \(k=1\).

Now assume \(p,q\ge k\). If \(q\ge k+1\), then \(q+d_i\ge k\) automatically for every \(i\). If \(q=k\), the first inequality is equivalent to \(d_i\ge0\) for all \(i\), which is exactly \(Q\subseteq P\). Likewise, if \(p\ge k+1\), the second inequality is automatic, while if \(p=k\) it is equivalent to \(P\subseteq Q\). This proves the structural characterization.

For the enumerator, first count the interior region \(p,q\ge k+1\), which contributes \(I_{n,k}(u)I_{n,k}(v)\). If \(p=k\), then \(P\subseteq Q\): choose \(P\) in \(inom nk\) ways and then choose any subset of the remaining \(n-k\) indices to enlarge \(Q\), giving
\[
inom nk(uv)^k(1+v)^{n-k}.
\]
The symmetric boundary \(q=k\) contributes \(inom nk(uv)^k(1+u)^{n-k}\). Their common diagonal \(P=Q\), \(|P|=k\), has been counted twice, so subtract \(inom nk(uv)^k\). Finally, when \(k=1\), add the two exceptional one-sided sets \(A\) and \(B\). This gives the stated bivariate formula. Setting \(u=v=x\) gives the univariate formula.

Every nonexceptional feasible set has \(p,q\ge k\), so \(|S|\ge2k\). Equality forces \(p=q=k\), and then the two boundary inclusions force \(P=Q\). There are \(inom nk\) such sets. For \(k=1\), the two one-sided exceptional sets have size \(n\ge3\), so they do not change the minimum. Therefore \(\gamma_{	imes k}(\operatorname{Cr}_n)=2k\) for all \(1\le k\le n\).

## Verification
A standalone checker exhaustively enumerates every subset of \(\operatorname{Cr}_n\) for \(3\le n\le8\) and every \(1\le k\le n\). It compares the definition \(|N[v]\cap S|\ge k\) against the structural criterion, checks every bivariate coefficient obtained from \((|S\cap A|,|S\cap B|)\), checks the univariate coefficients, and checks the minimum size and number of minimum sets. The checker returns:

`VERIFY_OK n_range=3..8 k_values=33 subset_checks=669888 criterion_checks=669888 bivariate_checks=199684 coefficient_checks=546 minimum_checks=33 max_order=16`

This finite census is a consistency check only; the proof above establishes the infinite statement.

## Relationship to prior work
Chang, Dorbec, Kim, Raspaud, Wang, and Zhao define \(k\)-tuple domination in closed-neighborhood form and study the upper \(k\)-tuple domination number, with general regular-graph bounds and complexity results for bipartite and chordal graphs. Their searchable full text contains no crown-graph treatment and no occurrence of the equivalent \(K_{n,n}\) minus a perfect matching family. The result here instead classifies every feasible \(k\)-tuple dominating set of every crown graph and gives the complete side-sensitive enumerator.

Database searches were also made under the aliases crown graph, \(K_{n,n}\) minus a perfect matching, bipartite Kneser graph \(H(n,1)\), and \(K_n\) tensor \(K_2\). The closest published-record matches concerned restrained domination of crown graphs, upper \(k\)-tuple domination of complete multipartite graphs, and \(k\)-tuple total domination of threshold graphs. None implies the present closed-neighborhood all-set classification: crown graphs are not complete multipartite for \(n\ge3\), restrained domination is a different predicate, and \(k\)-tuple total domination uses open neighborhoods.

## Limitations
The theorem is specific to crown graphs and uniform multiplicity \(k\). It does not classify weighted, nonuniform, total, restrained, or connected multiple-domination variants. The literature search found no equivalent all-\(k\), all-set crown formula, but obscure older sources could still contain a special case such as only \(k=2\) or only the scalar minimum; that residual bibliographic risk does not affect the proof.

## References
G. J. Chang, P. Dorbec, H. K. Kim, A. Raspaud, H. Wang, and W. Zhao, “Upper \(k\)-tuple domination in graphs,” *Discrete Mathematics & Theoretical Computer Science* 14:2 (2012), 285–292. DOI: 10.46298/dmtcs.593.

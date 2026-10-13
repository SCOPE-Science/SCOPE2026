# Exact generating-tuple census and birthday law for finite Heyting-chain powers

## Finding

For integers \(k\ge 2\), \(n\ge 1\), and \(r\ge 0\), let \(C_k=\{a_0=0<a_1<\cdots<a_{k-1}=1\}\) be the \(k\)-element Heyting chain. Equip \(H_{k,n}=C_k^n\) with coordinatewise lattice operations, constants, and Heyting implication
\[
a\to b=\begin{cases}1,&a\le b,\\ b,&a>b.\end{cases}
\]
An ordered tuple \((g_1,\ldots,g_r)\) generates \(H_{k,n}\) precisely when the following two conditions hold:

1. The \(n\) binary positivity words \(b_i=(\mathbf 1[g_j(i)>0])_{j=1}^r\), for \(1\le i\le n\), are pairwise different.
2. At **each** coordinate \(i\), every intermediate level \(a_1,\ldots,a_{k-2}\) appears among \(g_1(i),\ldots,g_r(i)\). This condition is vacuous when \(k=2\).

Let \(h_k(s)=\sum_{j=0}^{k-2}(-1)^j\binom{k-2}{j}(k-1-j)^s\) and let \(N_{k,n,r}\) be the number of ordered generating tuples. Then
\[
\boxed{N_{k,n,r}=n!\,[z^n]\prod_{s=0}^r\bigl(1+h_k(s)z\bigr)^{\binom rs}.}
\]
Here \([z^n]\) denotes coefficient extraction, and the usual convention \(0^0=1\) is used in the finite counting expression. The **exact** generator rank is
\[
\boxed{d(H_{k,n})=\min\Bigl\{r\ge0:n\le\sum_{s=k-2}^r\binom rs\Bigr\}.}
\]
Empty sums are zero. For \(k=2\) this specializes to \(N_{2,n,r}=(2^r)_{\underline n}\) and \(d(H_{2,n})=\lceil\log_2 n\rceil\).

There is also a sharp random-generation law. Choose all \(nr\) generator entries independently and uniformly from \(C_k\), keep \(k\) fixed, and let \(r\to\infty\) with \(n=n(r)\ge1\). Put
\[
p=\frac{k-1}{k},\qquad q=p^2+(1-p)^2,\qquad \mu_r=\binom n2 q^r.
\]
Then
\[
\boxed{\Pr\bigl(\langle g_1,\ldots,g_r\rangle=H_{k,n}\bigr)\longrightarrow e^{-\theta}}
\]
whenever \(\mu_r\to\theta\in[0,\infty]\), with \(e^{-\infty}=0\). In particular, the random threshold is \(r\approx 2\log n/\log(1/q)\), whereas the existence threshold satisfies \(d(H_{k,n})\sim\log_2 n\) for every fixed \(k\).

For example, \(H_{3,2}\) has exactly \(14\) ordered generating pairs; \(H_{4,2}\) has exactly \(168\) ordered generating triples. Also \(d(H_{5,2023})=12\), since the admissible positivity-word counts at lengths \(11\) and \(12\) are \(1981\) and \(4017\), respectively.

## Assumptions and scope

The signature is the **bounded Heyting** signature \((\wedge,\vee,\to,0,1)\), with no global modal quantifiers and no designated intermediate truth constants. Each generator is a function from the same labeled set of \(n\) coordinates to \(C_k\); ordered tuples are counted, including repeated entries. All exact formulas hold for the stated finite parameters, including \(r=0\). The probability theorem holds for a fixed chain size \(k\), not for \(k\) growing with \(r\). The algebra is the full direct product, not the free algebra in a variety.

## Proof

**Necessity of the level condition.** In a chain, each of \(\wedge\), \(\vee\), and \(\to\) returns one of its inputs or an endpoint \(0\) or \(1\); the two named nullary constants are endpoints. Therefore evaluation of a term at coordinate \(i\) cannot produce an intermediate level not present in the generator entries at \(i\). Full generation requires all such levels.

**Necessity of distinct positivity words.** For a tuple-valued expression \(f\), let \(Z(f)=\{i:f(i)=0\}\). The identities
\[
Z(f\wedge g)=Z(f)\cup Z(g),\qquad Z(f\vee g)=Z(f)\cap Z(g),\qquad Z(f\to g)=Z(g)\setminus Z(f)
\]
hold coordinatewise, with the appropriate zero sets for the constants. Thus membership of a coordinate in \(Z(t)\), for every term \(t\), depends only on its initial positivity word. Two coordinates with the same word can never be assigned different zero/nonzero statuses by a generated term, contrary to full generation.

**Sufficiency.** In any Heyting chain, \(\neg x=(x\to0)\) is \(1\) exactly when \(x=0\), and \(\neg\neg x\) is \(1\) exactly when \(x>0\). For each coordinate \(i\) form the Boolean selector
\[
e_i=\bigwedge_{j:b_i(j)=0}\neg g_j\ \wedge\ \bigwedge_{j:b_i(j)=1}\neg\neg g_j.
\]
Empty meets equal \(1\). Distinct positivity words imply \(e_i(i)=1\) and \(e_i(u)=0\) for all \(u\ne i\). Each intermediate level \(a_s\) is attained at coordinate \(i\) by some \(g_j\), so \(e_i\wedge g_j\) is supported on \(i\) and takes value \(a_s\) there. The selector itself supplies level \(1\) at \(i\), while the constant \(0\) supplies zero. Taking finite joins reconstructs an arbitrary tuple in \(C_k^n\).

**Enumeration.** Fix a binary positivity word having \(s\) positive positions. Each such position can be labeled by one of \(k-1\) positive chain levels. The word meets the local level condition exactly when all \(k-2\) intermediate levels occur. Inclusion–exclusion gives \(h_k(s)\) labelings. For each possible binary word, either omit it or choose one of its \(h_k(s)\) valid labelings; no word can be used twice because the words must be distinct. Multiplication produces the generating polynomial, and choosing and labeling \(n\) distinct words yields the coefficient formula. Such a word exists exactly when \(s\ge k-2\), so the number of available words is \(\sum_{s=k-2}^r\binom rs\). This proves the rank formula.

**Random law.** The positivity words are independent Bernoulli-\(p\) words in \(\{0,1\}^r\). Their pair-collision probability is \(q^r\), and the probability that \(v\) specified distinct words all coincide is \(t_v^r\), where \(t_v=p^v+(1-p)^v\). For every integer \(v>2\), strict monotonicity of finite-dimensional \(\ell_u\)-norms gives \(t_v<q^{v/2}\). Let \(Y\) count pairs of identical positivity words; then \(\mathbb EY=\mu_r\).

If \(\mu_r\to\theta\in(0,\infty)\), expand the fixed factorial moments of \(Y\) as sums over ordered families of distinct pair-collision events. Families of disjoint edges give the asymptotic factorial moments of a Poisson random variable of mean \(\theta\). Any family having a connected component on \(v\ge3\) coordinates contributes a total of order at most \(n^v t_v^r\) for that component, which vanishes because \(nq^{r/2}\) remains bounded and \(t_v/q^{v/2}<1\). Hence \(Y\) converges in distribution to Poisson\((\theta)\).

If \(\mu_r\to0\), a union bound gives \(\Pr(Y>0)\le\mu_r\to0\). If \(\mu_r\to\infty\), then \(\operatorname{Var}(Y)\le\mu_r+O(n^3t_3^r)\). Dividing by \(\mu_r^2\) gives a quantity tending to zero, because \(nq^{r/2}\to\infty\) and \(t_3/q^{3/2}<1\). Therefore \(\Pr(Y=0)\to0\).

It remains to compare absence of collisions with full generation. For each intermediate level and each coordinate, the probability that the level is missing from its \(r\) entries is \(p^r\). The union bound gives an error of at most \((k-2)np^r\). Whenever \(\mu_r\) stays bounded, \(nq^{r/2}\) also stays bounded (apart from the trivial one-coordinate case), while \(p/\sqrt q<1\); hence this error tends to zero. Combining these facts establishes all three probability regimes.

For fixed \(k\), \(\sum_{s=k-2}^r\binom rs=2^r-O(r^{k-3})\) when \(k\ge3\); the Boolean case has exactly \(2^r\). Therefore the deterministic rank is asymptotic to \(\log_2 n\).

## Verification

Run \(\texttt{python3 verify.py}\) in a standard Python environment. The script independently computes the generated subalgebra under all three non-nullary operations, compares full generation with the structural conditions on \(11{,}189\) ordered tuples, compares exhaustive successful-tuple counts with the generating-polynomial formula in \(36\) parameter cases, and verifies the exact rank boundary for \(693\) parameter choices. Its expected final message begins with \(\texttt{VERIFY\_OK}\). These finite tests corroborate the general proof and do not certify its asymptotic claims.

## Relationship to prior work

Martins and Moraschini (2023) develop finite Heyting-algebra generation through Esakia coloring and use it to study locally finite varieties. Their Coloring Theorem 3.3 is a general structural context, but the inspected article does not enumerate tuples generating a fixed direct power of a finite chain or give the birthday threshold.

Czédli (2024) studies generating **distributive-lattice reducts** of direct powers via unrelated copies of posets (Theorem 1). The studied language lacks Heyting implication, and the inspected theorem does not give the present per-coordinate level-coverage criterion or the weighted generating-tuple polynomial. As a point of comparison, Czédli reports \(18\) generators for the lattice-language \(2023\)-fold power of the five-element chain, while the present bounded Heyting signature has rank \(12\); the language difference includes both implication and designated endpoints.

Carai (first posted 2024) describes free Gödel algebras and coproducts by Esakia duality, giving the broader algebraic background without these direct-power generating-tuple and random-generation formulas. The exact inclusion–exclusion and biased birthday arguments here are elementary tools used for a new joint classification; neither tool alone is claimed as new.

## Limitations

No independent audit has been performed. The originality comparison covers the specifically inspected works and targeted searches; an older source on generating tuples of Heyting direct powers could contain an implicit antecedent. The random limit assumes fixed \(k\) and independent uniform generator entries. The result concerns the pure Heyting signature; adding global quantifiers changes the local truth-level condition and the finite census. All stated conclusions are mathematical claims supported by the written proof, not by exhaustive computation for arbitrary parameters.

## References

1. M. Martins and T. Moraschini, *On locally finite varieties of Heyting algebras*, arXiv:2306.15997, first posted 28 June 2023, especially Section 3 and the Coloring Theorem 3.3. https://arxiv.org/html/2306.15997v1
2. G. Czédli, *Sperner theorems for unrelated copies of posets and generating distributive lattices*, Ural Mathematical Journal 10(1) (2024), 44–60, DOI:10.15826/umj.2024.1.004, especially Theorem 1. https://umj.uran.ru/index.php/umj/article/download/668/pdf
3. L. Carai, *Free algebras and coproducts in varieties of Gödel algebras*, arXiv:2406.05480, first posted 8 June 2024, especially Sections 1, 3 and 4. https://arxiv.org/html/2406.05480v2

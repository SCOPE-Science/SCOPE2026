# Reversible block codes classify successor-reduct definitional equivalence in the irregular T(S) family

## Finding
Let \(L_0=\{0,\mathrm{suc}\}\). For an irregular set \(S\subseteq\omega\), Andréka, Madarász, Németi, and Székely consider
\[
T(S)=\{R(\mathrm{suc}^n(0)):n\in S\}\cup\{\neg R(\mathrm{suc}^n(0)):n\notin S\}\cup\operatorname{Th}(\langle\omega,0,\mathrm{suc}\rangle).
\]
Write \(s_n=1\) iff \(n\in S\), and similarly \(z_n\) for \(Z\).

Call \(T(S)\) and \(T(Z)\) **\(L_0\)-fixed definitionally equivalent** when, after giving their predicate symbols different names \(R_S,R_Z\), they have a joint definitional extension that leaves the symbols \(0,\mathrm{suc}\) unchanged. Equivalently, each predicate is explicitly definable from the other over the same successor skeleton, and the two definitions are inverse in the joint theory.

Then, for irregular \(S,Z\), the following are equivalent.

1. \(T(S)\) and \(T(Z)\) are \(L_0\)-fixed definitionally equivalent.
2. There are integers \(r,N\ge 0\) and a Boolean local rule
   \[
   f:\{0,1\}^{2r+1}\to\{0,1\}
   \]
   such that
   \[
   z_n=f(s_{n-r},\ldots,s_{n+r})\qquad(n\ge N),
   \]
   and the induced map \(F:\{0,1\}^{\mathbb Z}\to\{0,1\}^{\mathbb Z}\),
   \[
   F(x)_n=f(x_{n-r},\ldots,x_{n+r}),
   \]
   has an inverse given by another finite-radius local rule.

Thus the exact relative-equivalence relation is a **reversible-cellular-automaton tail relation**: arbitrary finite prefix changes are harmless, while every sufficiently remote coordinate must be produced by one fixed reversible local recoding.

Two immediate consequences are:

- every \(L_0\)-fixed equivalence class of irregular theories is countably infinite;
- since there are continuum many irregular sets, there are continuum many such equivalence classes.

At radius one there is a fully finite refinement. If both the forward and inverse eventual rules have radius one, the only possibilities are
\[
R'_n\in\{R_{n-1},R_n,R_{n+1},\neg R_{n-1},\neg R_n,\neg R_{n+1}\}
\]
outside a finite prefix.

## Assumptions and scope
The result is deliberately **relative to the common successor reduct** \(L_0=\{0,\mathrm{suc}\}\). It does not claim to classify unrestricted definitional equivalence after arbitrary renaming or redefinition of \(0\) and \(\mathrm{suc}\). The underlying sets \(S,Z\) are assumed irregular in the source paper's sense: every finite binary pattern occurs. The source proves that every such pattern in fact occurs infinitely often.

A “reversible finite-radius local rule” here means exactly a local rule whose global map on the two-sided full binary shift has a finite-radius local inverse; no symbolic-dynamics classification theorem is needed for the statement.

## Proof
### 1. Definability becomes an eventual block map
Suppose first that a joint definitional extension over \(L_0\) exists. Let \(\varphi(x)\) be the formula defining \(R_Z\) from \(R_S\). Evaluate it in the standard model
\[
\mathfrak N_S=\langle\omega,0,\mathrm{suc},S\rangle.
\]
Relationalize the successor function by its graph. The Gaifman graph then has degree at most two. By Gaifman locality, every one-variable first-order formula is a Boolean combination of a bounded-radius local formula around the free variable and finitely many background local sentences. In the fixed structure \(\mathfrak N_S\), those background sentences have fixed truth values. Hence there are \(r,N\) and a Boolean function \(f\) such that, for every \(n\ge N\),
\[
\mathfrak N_S\models\varphi(n)
\quad\Longleftrightarrow\quad
f(s_{n-r},\ldots,s_{n+r})=1.
\]
Because the \(R_Z\)-reduct of the joint model is a model of \(T(Z)\), its \(\mathbb N\)-part is exactly the characteristic sequence \(z\). Therefore
\[
z_n=f(s_{n-r},\ldots,s_{n+r})
\]
for all sufficiently large \(n\).

Applying the same argument to the inverse definition gives a radius \(q\), a local rule \(g\), and an index \(M\) with
\[
s_n=g(z_{n-q},\ldots,z_{n+q})
\]
for all \(n\ge M\).

### 2. Irregularity upgrades one tail identity to a full-shift inverse
Let \(F,G\) be the two-sided block maps induced by \(f,g\). Their composition \(H=G\circ F\) is another finite-radius local map. The inverse definitions in the joint definitional extension imply
\[
H(s)_n=s_n
\]
for all sufficiently large \(n\), in the sense that the local composition rule applied to the one-sided tail returns the center bit.

The source proves that every finite binary pattern occurs infinitely often in an irregular sequence. Let \(w\) be any binary block long enough to contain the whole neighborhood used by \(H\). Some occurrence of \(w\) lies beyond the finite exceptional prefix, so the local rule for \(H\) must return the center bit on \(w\). Since \(w\) was arbitrary, \(H\) is the identity on every point of \(\{0,1\}^{\mathbb Z}\).

The same argument, using irregularity of \(Z\), gives \(F\circ G=\mathrm{id}\). Thus \(F\) is a reversible finite-radius block code and \(G=F^{-1}\).

### 3. Every reversible tail block code gives a joint definitional extension
Conversely, suppose \(f\) induces a reversible block map \(F\), with finite-radius inverse rule \(g\), and suppose the displayed tail equation for \(z\) holds from some index onward.

A first-order formula can read any fixed finite window around \(x\): predecessors are expressed by equations of the form \(\mathrm{suc}^k(y)=x\), and successors are terms \(\mathrm{suc}^k(x)\). Hence the truth table of \(f\) gives a formula defining \(R_Z(x)\) at every point far enough from \(0\). The finitely many exceptional values near \(0\), as well as any additional finite prefix before the tail equation begins, are hard-coded using the named points
\[
0,\mathrm{suc}(0),\ldots,\mathrm{suc}^{N'}(0).
\]
This produces a single formula \(\varphi(x)\) whose interpretation in \(\mathfrak N_S\) is exactly \(Z\). The inverse rule \(g\), with another finite hard-coded prefix, produces a formula \(\psi(x)\) recovering \(S\) from \(Z\).

Now use completeness of \(T(S)\) and \(T(Z)\), proved as Lemma 1 in the source paper. Every sentence of \(T(Z)\), after replacing \(R_Z\) by \(\varphi\), is true in \(\mathfrak N_S\), hence belongs to \(T(S)\). Likewise the inverse translation sends \(T(S)\) into \(T(Z)\). The composition identities are true in the standard models, so by completeness they hold in every model. Therefore the theory obtained by adjoining
\[
\forall x\,[R_Z(x)\leftrightarrow\varphi(x)]
\]
to \(T(S)\) is a joint definitional extension over \(L_0\), with \(R_S\) explicitly recovered by \(\psi\).

This proves the equivalence.

### 4. Cardinality of the classes
There are only countably many finite-radius Boolean rules, only countably many thresholds \(N\), and only finitely many choices for a prefix of any fixed length. Hence each \(L_0\)-fixed equivalence class is countable.

It is infinite: the two-sided shift \(F(x)_n=x_{n+1}\) is reversible, so every finite left shift of the tail of \(S\), with any finite prefix filled in, lies in the same class. An irregular sequence cannot be eventually periodic, so infinitely many of these shifted tails are distinct. Since the source constructs continuum many irregular subsets of \(\omega\), the quotient has cardinality continuum.

### 5. Radius-one refinement
For a radius-one rule there are only \(2^8=256\) Boolean truth tables. If the inverse is also radius one, there are \(256^2\) candidate pairs. Checking the two composition identities requires only the \(2^5=32\) five-bit neighborhoods, because a composition of two radius-one rules has radius two. Exhaustive exact enumeration leaves precisely six inverse pairs, corresponding to left shift, identity, right shift, and their bit-complements.

## Verification
The bundled `verify.py` exhaustively checks all \(65{,}536\) ordered pairs of elementary binary radius-one rules. For every pair it tests both composition directions on all \(32\) five-bit words, giving \(4{,}194{,}304\) exact composition checks. It finds exactly the inverse pairs
\[
(15,85),(51,51),(85,15),(170,240),(204,204),(240,170),
\]
which are the three coordinate projections and their complements, paired with their local inverses. It then replays all six rules on a finite universal word containing every binary word through length eight. The run returns

`VERIFY_OK 4215844 exact assertions`.

The finite checker validates the radius-one refinement and the local-composition mechanism. The general theorem is established by the written locality and dense-pattern argument.

## Relationship to prior work
Andréka, Madarász, Németi, and Székely introduce the theories \(T(S)\), define irregularity, prove completeness for irregular \(S\), construct concrete isomorphisms between their model categories, and show that there are continuum many pairwise definitionally inequivalent theories. Their argument for continuum many inequivalent theories is cardinal: each definitional equivalence uses only finitely many formulas, so each theory can have at most countably many equivalents on a fixed finite signature. They do not identify which predicate recodings are possible when the common \(\{0,\mathrm{suc}\}\)-skeleton is required to stay fixed.

The present result supplies that missing exact classification for the reduct-fixed problem. The additional ingredient is standard Gaifman locality: on a successor path, a unary first-order definition is eventually a finite-window rule. Irregularity then promotes mutual tail definitions to mutually inverse block maps on the entire two-sided full shift.

Targeted literature searches for combinations of the source family with cellular automata, reversible block codes, joint definitional extensions over the successor reduct, and Gaifman locality found the motivating paper and unrelated symbolic-dynamics results, but no statement of this classification.

## Limitations
The theorem does not classify unrestricted definitional equivalence between \(T(S)\) and \(T(Z)\), because an unrestricted equivalence may also redefine or rename symbols in the common successor skeleton. The exact criterion is only for joint definitional extensions that keep \(0\) and \(\mathrm{suc}\) fixed.

The passage from formulas to eventual local rules uses standard Gaifman locality after relationalizing the successor function. The result is structural rather than algorithmic: it does not provide a practical decision procedure for whether two arbitrary infinite irregular sequences are in the same reversible-block-code tail class.

The radius-one list assumes both the forward rule and its inverse have radius one. The general theorem allows different and arbitrarily large finite radii.

## References
1. H. Andréka, J. Madarász, I. Németi, G. Székely, *Testing definitional equivalence of theories via automorphism groups*, arXiv:2211.14232; Review of Symbolic Logic 17 (2024), 1097–1118, DOI 10.1017/S1755020323000242. First arXiv submission: 25 November 2022.
2. L. Hella, L. Libkin, J. Nurmonen, *Notions of locality and their logical characterizations over finite models*, Journal of Symbolic Logic 64 (1999), 1751–1773, DOI 10.2307/2586810. Used as a reference for Gaifman locality and local normal forms.

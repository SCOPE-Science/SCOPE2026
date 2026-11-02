# Sharp period of binary orientable sequences of order eight

## Finding

The maximum period of a binary orientable cyclic sequence of order eight is exactly
\[
M_8=92.
\]
An orientable sequence here is a cyclic binary word in which no two length-eight cyclic windows are equal or reversals of one another. The lower bound is witnessed by the explicit cyclic word in `certificate.json`. The upper bound follows from an independently checkable, integral linear-inequality certificate in that file. The result closes the published interval \(92\le M_8\le96\).

## Assumptions and scope

A cyclic binary word of period \(m\) is indexed modulo \(m\); every starting position defines one window of length eight, including wraparound. All \(m\) windows must occupy distinct reversal classes, and no window may be a palindrome. No assumption of primitive period is needed: these conditions imply it.

Let \(E\) denote the 240 nonpalindromic binary words of length eight. For \(w\in E\), let \(w^R\) be its reversal, \(p(w)\) its length-seven prefix, and \(s(w)\) its length-seven suffix. The 120 unordered pairs \(\{w,w^R\}\) are indexed by their smaller eight-bit integer representations.

## Proof

For an arbitrary orientable cyclic word, let \(x_w\in\{0,1\}\) record whether \(w\) occurs among its cyclic windows. Each reversal class satisfies
\[
x_w+x_{w^R}\le1.
\]
The cyclic sequence traverses the order-seven de Bruijn graph using precisely these arcs; hence, for every seven-bit vertex \(v\),
\[
F_v(x)=\sum_{s(w)=v}x_w-\sum_{p(w)=v}x_w=0.
\]
Variables for palindromic eight-bit words are understood to be zero.

An additional integral constraint is decisive. If \(v\) is a palindromic seven-bit word, the two incoming arcs \(0v,1v\) are reversal-paired with outgoing arcs \(v0,v1\), respectively. At most one incoming arc and at most one outgoing arc may be selected: choosing both incoming arcs would, by balance, require both outgoing arcs and violate the two reversal-pair constraints. Thus the vertex is unused, or it has precisely one incoming and one outgoing arc, with their exterior bits opposite. Consequently, for both \(b\in\{0,1\}\),
\[
P_{v,b}(x)=x_{bv}-x_{v(1-b)}=0.
\]
The argument also covers self-loops, which are palindromic eight-bit words and therefore absent.

The accompanying `certificate.json` gives integers \(\alpha_v\) for seven-bit vertices, integers \(\mu_{v,b}\) for these palindrome identities, and nonnegative integers \(\beta_q\) for reversal pairs. Unlisted coefficients are zero. For every \(w\in E\), define
\[
\gamma_w=\beta_{\min(w,w^R)}+\alpha_{s(w)}-\alpha_{p(w)}
+\sum_{v=v^R}\sum_{b=0}^1
\mu_{v,b}\bigl(\mathbf1_{w=bv}-\mathbf1_{w=v(1-b)}\bigr).
\]
Here the minimum and subscripts for eight-bit words refer to their integer encodings. The exact certificate satisfies all 240 inequalities \(\gamma_w\ge1\) and \(\sum_q\beta_q=92\); `verify.py` checks these statements using integer arithmetic alone. Therefore
\[
\begin{aligned}
m=\sum_{w\in E}x_w
&\le\sum_{w\in E}\gamma_wx_w\\
&=\sum_q\beta_q(x_q+x_{q^R})
 +\sum_v\alpha_vF_v(x)
 +\sum_{v=v^R,b}\mu_{v,b}P_{v,b}(x)\\
&\le\sum_q\beta_q=92.
\end{aligned}
\]
This upper bound applies to every orientable cyclic word, whether or not its selected arcs form one connected graph.

For attainment, `certificate.json` supplies a 92-bit cyclic word. Directly enumerating its 92 wraparound windows proves that they are all nonpalindromic and represent 92 distinct reversal classes. Hence \(M_8\ge92\), completing the proof.

## Verification

From the directory containing `certificate.json`, run `python3 verify.py` with Python 3 and only its standard library. The program checks the size and reversal-class partition of \(E\), exhaustively verifies the local palindromic-vertex implication, checks every integer dual inequality, sums the dual weights, and checks all 92 windows of the witness. The expected output starts `VERIFY_OK M_8=92`. The proof does not rely on trusting an optimizer's log or an unbounded search.

## Relationship to prior work

Dai, Martin, Robshaw and Wild introduced binary orientable sequences and supplied a general upper bound. Gabrić and Sawada (2024), Table 1, report for order eight a constructed period of 92 and an upper bound of 96; their extending procedures are heuristic and do not prove optimality of that period. Mitchell and Wild's recursive construction gives length 80 at order eight. Later work on nonbinary orientable sequences and general bounds does not establish the binary order-eight optimum. The new ingredient here is an explicit exact upper certificate supported by a palindromic-vertex identity, rather than the previously known length-92 example.

## Limitations

This is a fixed-order result, not a formula for arbitrary orders. The certificate is finite and exact for order eight only; neither its 92-bit witness nor the finite check claims to classify every optimal word. The 1993 source chapter was not available in full text during comparison; its upper bound and historical role are checked against later primary literature. An unindexed earlier specialization remains a residual priority risk.

## References

1. D. Gabrić and J. Sawada, *Construction of orientable sequences in \(O(1)\)-amortized time per bit*, arXiv:2401.14341v1, first public January 25, 2024. https://arxiv.org/abs/2401.14341
2. D. Gabrić and J. Sawada, *Efficient Construction of Long Orientable Sequences*, CPM 2024, LIPIcs 296, article 15, Table 1 and Section 4. https://doi.org/10.4230/LIPIcs.CPM.2024.15
3. C. J. Mitchell and P. R. Wild, *Constructing orientable sequences*, arXiv:2108.03069v1 (August 6, 2021); IEEE Transactions on Information Theory 68 (2022). https://arxiv.org/abs/2108.03069
4. Z.-D. Dai, K. M. Martin, M. J. B. Robshaw and P. R. Wild, *Orientable sequences*, in *Cryptography and Coding III* (1993), pp. 97–115; discussed in references 1–3.
5. C. J. Mitchell and P. R. Wild, *New orientable sequences*, first public July 3, 2025; *Acta Informatica* 63 (2026). https://arxiv.org/abs/2507.02526

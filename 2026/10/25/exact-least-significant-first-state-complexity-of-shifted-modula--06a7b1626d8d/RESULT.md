# Exact least-significant-first state complexity of shifted modular valuation words

## Finding

Let \(b\ge2\) and \(m\ge2\) be integers. For positive integers \(x\), define the base-adic order \(\nu_b(x)\) to be the largest \(r\ge0\) for which \(b^r\mid x\). For each shift \(c\ge0\), consider the automatic sequence
\[f_c(n)=\nu_b(n+c+1)\bmod m,\qquad n\in\mathbb Z_{\ge0}.\]
Let \(N_{b,m}(c)\) be the number of states of the smallest *complete* deterministic finite automaton with output (DFAO) evaluating this function from a finite base-\(b\) representation read **least-significant digit first**. The output must be correct on every finite digit word, including the empty word and representations with extra high-order zeros.

**Theorem (exact translated valuation complexity).** With
\[L_b(c)=\min\{\ell\ge0:b^\ell\ge c+1\},\]
we have for every \(b,m,c\) in the stated ranges
\[\boxed{N_{b,m}(c)=L_b(c)+2m}.\]
Exactly \(L_b(c)+m\) of the minimal states are nonconstant residuals; the other \(m\) states are the distinct constant output functions. The nonconstant transition graph is a chain of length \(L_b(c)\) feeding an \(m\)-cycle. Every nonconstant state has precisely one digit leading to the next nonconstant state; its other digits lead to constant states.

For \(b=m=2\), the sequence at \(c=0\) is the classical binary period-doubling word (in the valuation convention). The formula becomes
\[N_{2,2}(0)=4,\qquad N_{2,2}(c)=5+\lfloor\log_2c\rfloor\quad(c\ge1).\]
Thus the exact state count changes only when a positive shift crosses a power of two.

## Assumptions and scope

A finite input \(d_0d_1\cdots d_{k-1}\), read least-significant digit first, represents the integer \(u=\sum_{j=0}^{k-1}d_jb^j\). The empty input represents \(0\). Outputs are in \(\{0,1,\dots,m-1\}\); all words are legal. For composite \(b\), \(\nu_b\) means divisibility by powers of the **whole base**, rather than the usual prime-adic valuation. All three parameters \(b,m,c\) are integers; no negative-shift, single-residue, or most-significant-first claim is made.

## Proof

**1. Residual classification.** After reading a word of length \(k\) with value \(u\), where \(0\le u<b^k\), any remaining suffix encoding \(n\ge0\) gives
\[R_{k,u}(n)=\nu_b(c+1+u+b^k n)\bmod m.\]
Put \(t=c+1+u>0\). If \(b^k\nmid t\), then \(j=\nu_b(t)<k\) and divisibility modulo \(b^{j+1}\) shows \(\nu_b(t+b^k n)=j\) for all \(n\); the residual is the constant \(C_j(n)=j\bmod m\). If \(b^k\mid t\), put \(s=t/b^k\ge1\). Then
\[R_{k,u}(n)=V_{s,k\bmod m}(n),\qquad V_{s,p}(n)=(p+\nu_b(n+s))\bmod m.\]
For each fixed \(k\ge0\), the condition \(u\equiv-(c+1)\pmod{b^k}\) selects **exactly one** \(u\) in \([0,b^k-1]\), so there is exactly one nonconstant residual at depth \(k\). Its shift is
\[s_k=\left\lceil\frac{c+1}{b^k}\right\rceil,\]
and its phase is \(k\bmod m\).

**2. Reachability and counting.** Let \(L=L_b(c)\). For \(0\le k<L\), we have \(s_k>1\) and \(s_{k+1}<s_k\); these \(L\) shifts are all distinct. For every \(k\ge L\), we have \(s_k=1\). As \(k\) runs through all sufficiently large integers, its phases exhaust every residue modulo \(m\). Therefore the nonconstant residuals consist of \(L\) distinct preperiodic functions and the \(m\) functions \(V_{1,p}\). To reach each constant \(C_p\), first reach \(V_{1,p}\) and then read digit \(0\): since \(\nu_b(1+bn)=0\), the resulting function is exactly \(C_p\). These exhaust the classification in Step 1, giving at most \(L+2m\) states.

For completeness, the corresponding transitions are explicit:
\[\delta(V_{s,p},d)=\begin{cases}V_{(s+d)/b,(p+1)\bmod m},&b\mid(s+d),\\ C_p,&b\nmid(s+d),\end{cases}\qquad \delta(C_p,d)=C_p.\]
Each \(s\ge1\) has exactly one digit \(0\le d<b\) satisfying \(b\mid(s+d)\), and the successor shift is \(\lceil s/b\rceil\). The output of \(V_{s,p}\) is \((p+\nu_b(s))\bmod m\); the output of \(C_p\) is \(p\). Initialize at \(V_{c+1,0}\). This is a finite complete DFAO using precisely the stated reachable states.

**3. Distinguishability (matching lower bound).** Constants \(C_p\) differ for different \(p\). No \(V_{s,p}\) is constant: for all sufficiently large \(r\), the nonnegative input \(n=b^r-s\) has \(V_{s,p}(n)=p+r\bmod m\), and consecutive \(r\)'s differ because \(m\ge2\). If \(s=t\) but \(p\ne p'\), then \(V_{s,p}\) and \(V_{t,p'}\) differ at every input.

Finally suppose \(s\ne t\). Put \(a=\nu_b(|t-s|)\). Choose any sufficiently large integer \(r>a\) with \(b^r\ge\max\{s,t\}\) and let \(n_r=b^r-s\). The elementary divisibility fact \(\nu_b(b^r+t-s)=a\) gives
\[V_{s,p}(n_r)=p+r\bmod m,\qquad V_{t,p'}(n_r)=p'+a\bmod m.\]
Repeating at \(r+1\), the first value changes by one modulo \(m\), whereas the second is unchanged. Since \(m\ge2\), the two residual functions cannot agree for both inputs. Thus all \(L+2m\) reachable residual functions are different. The usual residual-function characterization of minimal DFAOs gives the matching lower bound and proves the theorem. All valuation arguments remain valid when \(b\) is composite, because adding a multiple of \(b^{j+1}\) cannot change whether a positive integer divisible by \(b^j\) is divisible by \(b^{j+1}\).

## Verification

The embedded standard-library checker independently constructs the reachable transition graph from the arithmetic state rules, refines Moore-equivalence classes until minimal, and compares its outputs against direct integer valuations. The recorded run tested \(3{,}200\) parameter triples, covering bases \(2\) through \(6\), moduli \(2\) through \(5\), shifts \(0\) through \(150\), and nine additional boundary shifts. It also compared \(204{,}800\) direct outputs. All checks passed. This finite testing is supplementary; the all-parameter statement is proved by Steps 1–3.

To reproduce: run `python3 checks/verify_shifted_valuations.py` in the directory containing the extracted package. The recorded output is in `checks/verification_output.txt`.

## Relationship to prior work

Zantema and Bosma (2022, §§5 and 7) study minimal automata for automatic sequences and general operations, proving state-complexity bounds for taking tails and arithmetic subsequences. Their general bounds do not identify the minimal states of the family \(\nu_b(n+c+1)\bmod m\) or the exact formula above. Moradi, Rampersad and Shallit (arXiv:2512.10017, first submitted 2025-12-10, §4) study state complexity of linear subsequences of automatic sequences, principally in most-significant-digit-first format. Moradi, Popoli, Shallit and Vukusic (arXiv:2603.18858, first submitted 2026-03-19, §3) analyze shifts of the Fibonacci word in Zeckendorf numeration, establishing logarithmic-order results in a different numeration system. These works motivate the exact shifted-state question but do not entail the formula for base-adic valuation residues. The binary period-doubling specialization is a familiar sequence; the contribution is the uniform shifted minimal-state law and its complete residual graph.

## Limitations

The formula is about complete least-significant-first DFAOs on *all* finite digit words, not an arbitrary convention restricting inputs to canonical representations. The residue modulus must satisfy \(m\ge2\): for \(m=1\) the word is constant and one state suffices. Negative shifts and other numeration systems are outside scope. The literature comparison cannot exclude every unindexed equivalent valuation-kernel computation; independent mathematical and historical validation has not been performed.

## References

1. H. Zantema and W. Bosma, *Complexity of automatic sequences*, Information and Computation 288 (2022), article 104710. https://doi.org/10.1016/j.ic.2021.104710 . Accessible author PDF: https://www.math.ru.nl/~bosma/pubs/Zantema_Bosma_Complexity_of_Automatic_Sequences.pdf .
2. D. Moradi, N. Rampersad, and J. Shallit, *Complexity of Linear Subsequences of \(k\)-Automatic Sequences*, arXiv:2512.10017, first public submission 2025-12-10. https://arxiv.org/abs/2512.10017 .
3. D. Moradi, P. Popoli, J. Shallit, and I. Vukusic, *State Complexity of Shifts of the Fibonacci Word*, arXiv:2603.18858, first public submission 2026-03-19. https://arxiv.org/abs/2603.18858 .

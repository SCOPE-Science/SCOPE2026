# Independent mathematical audit

## correctness

PASS

For p<=r Schemmel S_r(p²)=0 outside positive domain. For r=1 use m=6 when p=2, and m=2p² otherwise. For r>=2 let a>r be least prime, δ=a-r. δ=1 uses m=ap² for p!=a, or m=ab for p=a and next prime b<2a. For δ>=2 set L=p²/a and U=r+p(p-r)/δ; source algebra simplifies after a=r+δ to 5δa(U-7L/5)=δa(3r-2δ)+a(5r-4δ)(p-a)+(5r-2δ)(p-a)²>0. Source consecutive-prime bound q/t<=7/5 outside 2->3,3->5,7->11 gives q<=U, m=aq>p² and S_r(m)<=S_r(p²); only (r,p)=(3,7),(5,7) require explicit 55,77. Independent SymPy simplification and 5,249 tested r,p witnesses agree. The universal proof relies on the cited published consecutive-prime ratio lemma; finite checking is corroborative only.

## originality

PASS

Defant 2014 Section 3 states the prime-square assertion as Conjecture 3.1 and only proves restricted prime-power exclusions; no later universal proof found in direct broad literature and Resultary searches. This gives a genuine named conjecture resolution subject to unindexed priority risk.

## value

PASS

Uniformly proves a specifically posed open conjecture about sparse minima of multiplicative Schemmel totient sequences, with an explicit uniform larger witness construction and delicate prime-gap exceptional cases; not a textbook restatement of an existing theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.

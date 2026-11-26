# Independent mathematical audit

## correctness

PASS

The source's system (2.2) resets B=(h1,yB) to ((1+p1)h1,yB−tau1); the successor map must therefore use f(A)=yB−tau1−yA. Theorem 3.1 instead prints yB(1−p1)−yA. In the strict case the model gives f(A)>0. The printed argument asks for f(A1)<0, chooses an impact height yB1>yB, and prints f(A1)=yB1−yB>0 before applying the intermediate value theorem. The same-sign printed values do not imply a zero. Even the corrected f(A1)=yB1−tau1−yA1 has no negative sign established by yB1>yB alone. In the equality case the admissible first return closes at A. This is a diagnosis of the printed argument, not a counterexample to the theorem or to its numerical example. The supplied checker was inspected as an algebraic witness only; the conclusion follows directly from the source reset and proof.

## originality

PASS

The source contains the faulty inference, not its diagnosis. No distinct record or prior correction establishing this particular proof gap was found in the bounded checks. The generic successor-function method and intermediate value theorem are not claimed as new.

## value

PASS

This is not merely a mismatched sign character: the published existence proof for the strict case ends without its needed lower endpoint (and uses a different reset in the same argument). Identifying that missing obligation tells users of the theorem what must be established before relying on it, while separating the valid direct equality case and not mislabeling the theorem itself as false.

The dated certificate retains the supplied scientific assessment, sources and limitations.
